class content():

    folder_button_xpath="/html/body/div[2]/div[1]/div[2]/div[1]/div/div[2]/img"

    def __init__(self,driver):
        self.driver=driver

    def test_CFOclick(self,icon):
        self.driver.find_element_by_xpath=(self.folder_button_xpath).click()
