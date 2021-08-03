import random


class LoginPage:

    textbox_username_id="auth_login_id"
    textbox_password_id="auth_password"
    button_login_xpath="//input[@class='Login_Btn']"
 #   button_login_xpath="//input[@class='button-1 login-button']"
    button_logout_xpath="/html/body/header/div/div/div/div/div[2]/ul/li[3]/form/a/span/input[2]"
 #   link_logout_linktext="Logout"
    img_folder_xpath = "/html/body/div[2]/div[1]/div[2]/div[1]/div/div[2]/img"
    button_select_to_add_xpath="/html/body/div[3]/div[3]/div/div[2]/div[8]/a"
    button_create_folder_id = "createFolderBtn"
    img_player_css="#div_PlayerSelection > div.modal-dialog > div > div"
    img_player_id = "btn_SelectedPlayerNormal"

    textbox_content_name_id="folderIdTxt"
    textbox_description_id="folderDesTxt"
    button_add_id="addBtn"
    dropdown_foldertype_id="dd_folderType"


    def __init__(self, driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

    def clickContentFolderManagement(self): #clicking content folder from dashboard
        self.driver.find_element_by_xpath(self.img_folder_xpath).click()

    def clickSelectToAdd(self): #clicking 3lines to add
        self.driver.find_element_by_xpath(self.button_select_to_add_xpath).click()

    def clickCreateContentFolder(self): #Clicking to Add content
        self.driver.find_element_by_id(self.button_create_folder_id).click()

    def clickPlayerType(self):
        self.driver.find_element_by_css_selector (self.img_player_css)

    def clickPlayer(self):
        self.driver.find_element_by_id(self.img_player_id).click()

    def mediaFileName(self):
        self.driver.find_element_by_id(self.textbox_content_name_id).send_keys("Media11")

    def mediaDescription(self):
        self.driver.find_element_by_id(self.textbox_description_id).send_keys("This is a Media Description")

    def clickAddCreatedContent(self):
        self.driver.find_element_by_id(self.button_add_id).click()

    def scrollMessageName(self):
        self.driver.find_element_by_id(self.textbox_content_name_id).send_keys("Scrl11")

    def scrollMsgDescription(self):
        self.driver.find_element_by_id(self.textbox_description_id).send_keys("This is a Scroll Msg Description")

    def folderType(self):
        self.driver.find_element_by_id(self.dropdown_foldertype_id).click()

    def audioName(self):
        self.driver.find_element_by_id(self.textbox_content_name_id).send_keys("Audio1")

    def audioDescription(self):
        self.driver.find_element_by_id(self.textbox_description_id).send_keys("This is a Audio Description")

