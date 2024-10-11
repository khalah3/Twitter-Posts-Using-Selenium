#This code will bring the Post message on twitter to post a complain about upload and download speeds.

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

class BOT:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.Promised_down = 150
        self.Promised_up = 10


    def Get_Internet_Speed(self):
        self.driver.get(url='https://www.speedtest.net')
        start_test=self.driver.find_element(By.CLASS_NAME, value="start-text")
        start_test.click()
        time.sleep(50)
        self.download_speed=self.driver.find_element(By.CSS_SELECTOR,'.download-speed')
        self.upload_speed=self.driver.find_element(By.CSS_SELECTOR,'.upload-speed')
        return self.download_speed,self.upload_speed

    def Tweet_At_Provider(self):
        user = 'user@gmail.com'
        secret = 'password'
        username='user'
        self.driver.get(url='https://x.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJteCI6IjIifQ%3D%3D%22%7D')
        time.sleep(5)
        username = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        time.sleep(3)
        username.click()
        username.send_keys('user@gmail.com',Keys.ENTER)
        time.sleep(5)

        try:
            password = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
            time.sleep(3)
            password.click()
            password.send_keys('password',Keys.ENTER)
        except NoSuchElementException:
            username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            time.sleep(3)
            username.click()
            username.send_keys('user',Keys.ENTER)
            password = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.NAME, "password")))
            time.sleep(3)
            password.click()
            password.send_keys('password',Keys.ENTER)
            time.sleep(5)
        self.post_box = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Post")))
        self.post_box.click()
        self.post_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up"
                                  f" when i pay for {self.PROMISED_DOWN}down/{self.PROMISED_UP}up?")
        self.post = self.driver.find_element(By.CSS_SELECTOR, value="button[data-testid='tweetButtonInline']")
        self.post.click()
        time.sleep(10)




bot=BOT()
bot.Get_Internet_Speed()
bot.Tweet_At_Provider()
