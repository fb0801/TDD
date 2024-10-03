import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from datetime import datetime

SCREEN_DUMP_LOCATION = Path(__file__).absolute().parent / "screendumps"
MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')  
        if staging_server:
            self.live_server_url = 'http://' + staging_server 

    def tearDown(self):
        if self._test_has_failed():
            if not SCREEN_DUMP_LOCATION.exists():
                SCREEN_DUMP_LOCATION.mkdir(parents=True)
            self.take_screenshot()
            self.dump_html()
        self.browser.quit()
        super().tearDown()

    def _test_has_failed(self):
        # slightly obscure but couldn't find a better way!
        return self._outcome.result.failures or self._outcome.result.errors

    def wait(fn):
        def modified_fn(*args, **kwargs):  
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)  
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)
        return modified_fn 

    
    @wait
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID,'id_list_table')
                rows = table.find_elements(By.TAG_NAME,'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    @wait
    def wait_for(self, fn):
        return fn()

    def get_item_input_box(self):
        return self.browser.find_element(By.ID,'id_text')
    
    
    
    @wait
    def wait_to_be_logged_in(self, email):
        self.browser.find_element(By.LINK_TEXT,'Log out')
        
        navbar = self.browser.find_element(By.CSS_SELECTOR,'.navbar')
        self.assertIn(email, navbar.text)

    def wait_to_be_logged_in(self, email):
        self.browser.find_element(By.LINK_TEXT,'Log out')

    @wait
    def wait_to_be_logged_out(self, email):
        self.wait_for(
            lambda: self.browser.find_element(By.NAME,'email')
        )
        navbar = self.browser.find_element(By.CSS_SELECTOR,'.navbar')
        self.assertNotIn(email, navbar.text)

    def add_list_item(self, item_text):
        num_rows = len(self.browser.find_element(By.CSS_SELECTOR,'#id_list_table tr'))
        self.get_item_input_box().send_keys(item_text)
        self.get_item_input_box().send_keys(Keys.ENTER)
        item_number = num_rows + 1
        self.wait_for_row_in_list_table(f'{item_number}: {item_text}')


    def take_screenshot(self):
        path = SCREEN_DUMP_LOCATION / self._get_filename("png")
        print("screenshotting to", path)
        self.browser.get_screenshot_as_file(str(path))

    def dump_html(self):
        path = SCREEN_DUMP_LOCATION / self._get_filename("html")
        print("dumping page HTML to", path)
        path.write_text(self.browser.page_source)

    def _get_filename(self, extension):
        timestamp = datetime.now().isoformat().replace(":", ".")[:19]
        return (
            f"{self.__class__.__name__}.{self._testMethodName}-{timestamp}.{extension}"
        )