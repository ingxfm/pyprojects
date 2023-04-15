# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='/snap/bin/chromium')
# driver.get('http://selenium.dev')
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

chrome_webdriver_path = os.environ['CWDPATH']
driver = webdriver.Chrome(executable_path=chrome_webdriver_path)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
