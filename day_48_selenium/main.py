# built-in
import os
from time import sleep

# 3rd-party
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_driver_path = os.environ['CWDPATH']
service = Service(executable_path=chrome_driver_path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
# driver.get('https://www.amazon.com/dp/B08PPZWNCV/ref=twister_B09T3SWGTW?_encoding=UTF8&psc=1')
# price = driver.find_element(By.CLASS_NAME, 'apexPriceToPay')
# print(price.text)

# search_box = driver.find_element(By.NAME, value='field-keywords')
# print(search_box.tag_name)
# print(search_box.get_attribute('name'))

# logo = driver.find_element(By.CLASS_NAME, value='nav-logo-link')
# print(logo.size)

# 'http://www.python.org')
# doc_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# print(doc_link.text)

# bug_link = driver.find_element(By.XPATH, value='/html/body/div/footer/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

events_dict: dict = {}
events_list = []

# another way
date = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li time')
event_text = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

for i in range(len(date)):
    events_dict[f'{i}'] = {'time': f'{date[i].text}',
                           'name': f'{event_text[i].text}'}

print(events_dict)

# for i in range(5):
#     date = driver.find_element(By.XPATH, value=f'/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li[{i+1}]/time')
#     event = driver.find_element(By.XPATH, value=f'/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li[{i+1}]/a')
#     events_dict[f'{i}'] = {'time': f'{date.text}',
#                            'name': f'{event.text}'}
#
# print(events_dict)





sleep(1)
driver.quit()
