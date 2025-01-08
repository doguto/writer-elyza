from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
import time
import sys
sys.path.append('../../')
import environmental_variables as ev
from src.novel.novel import Novel, BasicInfo, Story


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


    def make_new_novel(self, basicInfo: BasicInfo):
        # move to page to make new novel
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[1]/a[1]').click()
        # write novel's info
        self.driver.find_element(By.XPATH, '//*[@id="NovelTitle"]').send_keys(basicInfo.title)
        self.driver.find_element(By.XPATH, '//*[@id="NovelAbstract"]').send_keys(basicInfo.description)
        # genre for HOT ranking
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="NovelHotRankGenre"]'))
        select.select_by_value(str(basicInfo.genre))
        # category
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="NovelCategoryId"]'))
        select.select_by_value(str(basicInfo.category))
        # novel's length
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="NovelVolume"]'))
        select.select_by_value(str(basicInfo.length))
        # current writing state
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="NovelComplete"]'))
        select.select_by_value(str(basicInfo.state))
        # Regularion(such as R-15)
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="NovelRSitei"]'))
        select.select_by_value(str(basicInfo.regulation))
        # tags
        for i in range(len(basicInfo.tags)):
            if i >= 10:
                break
            
            try:
                element = self.driver.find_element(
                    By.XPATH, 
                    f'//*[@id="NovelMypageSaveForm"]/div[8]/div/div[{i+1}]/input'
                )
                element.send_keys(basicInfo.tags[i],'\n')
            except:
                print('error')

        # create novel
        self.driver.find_element(By.XPATH, '//*[@id="NovelMypageSaveForm"]/div[11]/div/input').click() 


    def make_new_story(self, story: Story, chapter='', is_new_chapter=False):
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="ContentBlockEpisodeNovelTitle"]').send_keys(story.title)
        self.driver.find_element(By.XPATH, '//*[@id="NovelEpisodeBodyId"]').send_keys(story.text)
        if chapter == '':  # no chapter
            self.driver.find_element(By.XPATH, '//*[@id="ContentBlockEpisodeNovelMypageSaveEpisodeForm"]/div[4]/div[2]/input').click()
            return
        # chapter setting
        if is_new_chapter:
            self.driver.find_element(By.XPATH, '//*[@id="ContentBlockEpisodeNovelMypageSaveEpisodeForm"]/div[1]/div/a').click()
            self.driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/input').send_keys(chapter)
            self.driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div[4]/div/button[2]').click()
            time.sleep(1)
            Alert(self.driver).accept()
            # self.driver.
        else:
            self.driver.find_element(By.XPATH, '//*[@id="ContentBlockEpisodeNovelChapter"]').click()
            for i in range(2, 1000):  # 1000 is just a large number.
                chapterElement = self.driver.find_element(By.XPATH, f'//*[@id="ContentBlockEpisodeNovelChapter"]/option[{i}]')
                if not chapterElement.text == chapter:
                    continue
                chapterElement.click()
                break
        self.driver.find_element(By.XPATH, '//*[@id="ContentBlockEpisodeNovelMypageSaveEpisodeForm"]/div[4]/div[2]/input').click()
        

    # home is management my novels page
    def back_to_home(self):
        self.driver.find_element(By.XPATH, '//*[@id="navbar"]/div/div[2]/div[3]/a').click()


    def move_to_edit_page(self, basicInfo: BasicInfo):
        for i in range(2, 1000):  # 1000 is just a large number.
            titleElement = self.driver.find_element(By.XPATH, f'//*[@id="main"]/div[3]/div[{i}]/div[3]/div[1]/h2')
            if not titleElement.text == basicInfo.title:
                continue
            
            self.driver.find_element(By.XPATH, f'//*[@id="main"]/div[3]/div[{i}]/div[3]/div[2]/div[1]/a').click()
            break
