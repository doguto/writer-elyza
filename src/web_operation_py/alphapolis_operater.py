from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys
sys.path.append('../../')
import environmental_variables as ev
from src.novel.novel import Novel


# [WARNING] Default position is my novel management page.
class AlphapolisOperaterPy():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def sign_in(self):
        # Loginページの起動
        self.driver.get('https://www.alphapolis.co.jp/login')
        # Login情報入力
        self.driver.find_element(By.NAME,"email").send_keys(ev.EMAIL_ADDRESS)
        self.driver.find_element(By.NAME,"password").send_keys(ev.PASSWORD)
        # Login
        self.driver.find_element(By.XPATH, '//*[@id="UserLoginForm"]/div[3]/div/div[1]/input').click()
        # move to page to manage my novels
        self.driver.find_element(By.XPATH, '//*[@id="sidebar"]/div[2]/ul/li[2]/a').click()

    def make_new_works(self, novelBasicInfo:Novel.BasicInfo):
        # move to page to make new novel
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[1]/a[1]').click()
        # write novel's info
        self.driver.find_element(By.XPATH, '//*[@id="NovelTitle"]').send_keys(novelBasicInfo.title)
        self.driver.find_element(By.XPATH, '//*[@id="NovelAbstract"]').send_keys(novelBasicInfo.description)
        # genre for HOT ranking
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="NovelHotRankGenre"]'))
        select.select_by_value(str(novelBasicInfo.genre))
        # category
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="NovelCategoryId"]'))
        select.select_by_value(str(novelBasicInfo.category))
        # novel's length
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="NovelVolume"]'))
        select.select_by_value(str(novelBasicInfo.length))
        # current writing state
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="NovelComplete"]'))
        select.select_by_value(str(novelBasicInfo.state))
        # Regularion(such as R-15)
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="NovelRSitei"]'))
        select.select_by_value(str(novelBasicInfo.regulation))
        # tags
        for i in range(len(novelBasicInfo.tags)):
            if i >= 10:
                break
            
            try:
                element = self.driver.find_element(
                    By.XPATH, 
                    f'//*[@id="NovelMypageSaveForm"]/div[8]/div/div[{i+1}]/input'
                )
                element.send_keys(novelBasicInfo.tags[i],'\n')
            except:
                print('error')

        # create novel
        self.driver.find_element(By.XPATH, '//*[@id="NovelMypageSaveForm"]/div[11]/div/input').click() 
