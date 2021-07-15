import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL="http://localhost/webapp/eSignageS/login/tenant.ejs"
    username="admin"
    password="admin"

    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="e-Signage S - Login":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        if act_title=="e-Signage S - eSignage S - Dashboard":
            assert True
        else:
            assert False

    def test_content_folder_management(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()


