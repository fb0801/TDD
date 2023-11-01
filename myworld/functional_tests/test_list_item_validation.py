from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest
from selenium.webdriver.common.by import By

class ItemValidationTest(FunctionalTest):
    
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID,'id_new_item').send_keys(Keys.ENTER)


        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        self.wait_for(lambda: self.assertEqual( 
            self.browser.find_element(By.CSS_SELECTOR,'.has-error').text,  
            "You can't have an empty list item"  
        ))

        # She tries again with some text for the item, which now works
        self.fail('finish this test!')
        