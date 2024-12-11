# seleniumの必要なライブラリをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.append('../../')
import environmental_variables as ev


class AlphapolisOperaterPy():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        # Loginページの起動
        self.driver.get('https://www.alphapolis.co.jp/login')
        # Login情報入力
        self.driver.find_element(By.NAME,"email").send_keys(ev.EMAIL_ADDRESS)
        self.driver.find_element(By.NAME,"password").send_keys(ev.PASSWORD)
        # Login
        self.driver.find_element(By.XPATH, '//*[@id="UserLoginForm"]/div[3]/div/div[1]/input').click()


