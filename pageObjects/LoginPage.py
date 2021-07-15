class LoginPage:

    textbox_username_id="auth_login_id"
    textbox_password_id="auth_password"
    button_login_xpath="//input[@class='Login_Btn']"
 #   button_login_xpath="//input[@class='button-1 login-button']"
    button_logout_xpath="/html/body/header/div/div/div/div/div[2]/ul/li[3]/form/a/span/input[2]"
 #   link_logout_linktext="Logout"

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

