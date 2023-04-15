# built-in
import os
from time import sleep

# 3rd-party
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = os.environ['CWDPATH']
service = Service(executable_path=chrome_driver_path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)


# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# article_count = driver.find_element(By.ID, value='articlecount')
# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# article_count.click()

# # clicking
# all_portals = driver.find_element(By.LINK_TEXT, value='All portals')
# all_portals.click()
#
# # typing
# search_box = driver.find_element(By.NAME, value='search')
# search_box.send_keys('Python')
# search_box.send_keys(Keys.ENTER)

driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element(By.NAME, value='fName')
first_name.send_keys('John')
last_name = driver.find_element(By.NAME, value='lName')
last_name.send_keys('Kusack')
mail_address = driver.find_element(By.NAME, value='email')
mail_address.send_keys('john.kusack@prop.com')
button = driver.find_element(By.CSS_SELECTOR, value='button')
button.click()





sleep(3)
driver.quit()
