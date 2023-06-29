from selenium import webdriver

browser = webdriver.Firefox(executable_path="D:\\Program Files (x86)\\selenium_driver\\geckodriver.exe")
browser.get('http://localhost:8000')

assert 'Django' in browser.title


