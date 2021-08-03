import time
from pageObjects.LoginPage import LoginPage
from pageObjects.ContentFolderManagement import contentFolderManage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Test_002_ContentFolderManagement:
    baseURL="http://localhost/webapp/eSignageS/login/tenant.ejs"
    username="admin"
    password="admin"

    def test_content_folder_management(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.driver.implicitly_wait(10)
        self.lp.clickContentFolderManagement()

####### Media file creation ######
        time.sleep(2)
        self.lp.clickSelectToAdd()
        time.sleep(2)
        self.lp.clickCreateContentFolder()
        time.sleep(2)
        self.driver.switch_to.frame(self.lp.clickPlayerType())
        self.lp.clickPlayer()
        self.lp.mediaFileName()
        self.lp.mediaDescription()
        self.lp.clickAddCreatedContent()
####### Scroll Message file creation ######
        time.sleep(2)
        self.lp.clickSelectToAdd()
        time.sleep(2)
        self.lp.clickCreateContentFolder()
        time.sleep(2)
        self.driver.switch_to.frame(self.lp.clickPlayerType()) #player type
        self.lp.clickPlayer() # select player
        time.sleep(2)
        self.lp.audioName()

        #element=self.lp.folderType()
        #drp=Select(element)
        #drp.select_by_visible_text('Scroll Message')
        #drp.options()
        element = self.driver.find_element_by_id("dd_folderType")
        drp = Select(element)
        drp.select_by_visible_text('Audio')
#        drp.select_by_index(1)
   #     drp.select_by_value('PC-MAIN')
        time.sleep(2)
        self.lp.audioDescription()
        self.lp.clickAddCreatedContent()
        self.driver.close()
####### Scroll Message creation #######
        time.sleep(2)
        self.lp.clickSelectToAdd()
        time.sleep(2)
        self.lp.clickCreateContentFolder()
        time.sleep(2)
        self.driver.switch_to.frame(self.lp.clickPlayerType())  # player type
        self.lp.clickPlayer() # select player
        time.sleep(2)
        self.lp.scrollMessageName()
        time.sleep(2)
        element = self.driver.find_element_by_id("dd_folderType")
        drp = Select(element)
        drp.select_by_visible_text('Scroll Message')
        time.sleep(2)
        self.lp.scrollMsgDescription()
        self.lp.clickAddCreatedContent()
        self.driver.close()
