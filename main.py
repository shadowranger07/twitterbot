from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 20
PROMISED_UP = 20
chrome_driver_path = "/Users/adithya/Development/chromedriver"
TWTTR_EMAIL = "adithyagh.testing@gmail.com"
TWTTR_PSWD = "m@yercomplins14"
TWTTR_URL = "https://twitter.com/"
TWTTR_URL1 = "https://twitter.com/i/flow/login"
FAST_URL = "https://fast.com/"
TWTTR_USERNAME = "jhnmyrcmplns"


class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.up = 0
        self.down = 0
        self.list_speed = []

    def get_internet_speed(self, url):
        self.driver.get(url)
        time.sleep(20)
        self.up = self.driver.find_element(By.CSS_SELECTOR,
                                           "div#speed-value")
        button = self.driver.find_element(By.CSS_SELECTOR, "a#show-more-details-link")
        button.click()
        time.sleep(20)
        self.down = self.driver.find_element(By.CSS_SELECTOR,
                                             "span#upload-value")
        self.list_speed.append(int(self.down.text))
        self.list_speed.append(int(self.up.text))
        return self.list_speed
        # print(f"{self.down.text}, {self.up.text}")

    def tweet_at_provider(self, url, url1):
        self.driver.get(url)
        time.sleep(1)
        login = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div['
                                         '1]/a/div/span/span')
        login.click()
        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                         '2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        next_btn = self.driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                            '2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        email.send_keys(TWTTR_EMAIL)
        next_btn.click()
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div['
                                                      '2]/div/input')
        username.send_keys(TWTTR_USERNAME)
        next_btn1 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        next_btn1.click()
        time.sleep(2)
        pswd = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div['
                                                  '2]/div[1]/input')
        pswd.send_keys(TWTTR_PSWD)
        next_btn2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        next_btn2.click()
        time.sleep(5)
        write = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                   '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                   '1]/div/div/div/div[2]/div['
                                                   '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                                   '1]/div/div/div/div/div/div[2]/div/div/div/div')
        write.click()
        message = self.driver.find_element(By.CSS_SELECTOR, 'div.notranslate.public-DraftEditor-content')
        message_text = f"Hey Internet Provider, why is my internet speed {speed_list[0]}down/{speed_list[1]}up when I " \
                       f"pay for 150down/10up?"
        message.send_keys(message_text)
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        post.click()


bot = InternetSpeedTwitterBot()

speed_list = bot.get_internet_speed(FAST_URL)
if speed_list[0] < 100 or speed_list[1] < 100:
    bot.tweet_at_provider(TWTTR_URL, TWTTR_URL1)
