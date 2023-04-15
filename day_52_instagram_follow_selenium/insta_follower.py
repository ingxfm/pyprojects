# built-in
import os
import time
from time import sleep
import random

# 3rd-party
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = os.environ['CWDPATH']
URL_LOGIN = os.environ['INSTA']
URL_POLAR_BEAR = os.environ['POLAR']
USERNAME = os.environ['USER']
PASSWORD = os.environ['PASS']
SCROLL_DOWNS = 5


class InstaFollower:

    def __init__(self):
        service = Service(executable_path=CHROME_DRIVER_PATH)
        options = Options()
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self):
        self.driver.get(URL_LOGIN)
        ad_pop_up = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/button[2]')
        ad_pop_up.click()
        sleep(2)
        username_box = self.driver.find_element(By.NAME, value='username')
        username_box.send_keys(USERNAME)
        password_box = self.driver.find_element(By.NAME, value='password')
        password_box.send_keys(PASSWORD)
        sleep(1)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()
        sleep(5)
        not_now_button = self.driver.find_element(By.XPATH,
                                                  value='//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()
        sleep(2)

    def find_followers(self):
        followers_button = self.driver.find_element(By.XPATH,
                                                    value='/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span')
        followers_button.click()
        sleep(2)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div/div/div/div[2]')
        for i in range(SCROLL_DOWNS):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='li button')
        for button in all_buttons:
            try:
                button.click()
                delay_clicks = random.randint(95, 201)/100
                sleep(delay_clicks)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,
                                                         value='/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()

    def terminate_window(self):
        self.driver.quit()
