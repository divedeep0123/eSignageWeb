class contentFolderManage():

    img_folder_xpath = "/html/body/div[2]/div[1]/div[2]/div[1]/div/div[2]/img"
    button_select_to_add_xpath="/html/body/div[3]/div[3]/div/div[2]/div[8]/a"
    button_create_folder_id = "createFolderBtn"
    img_player_css="#div_PlayerSelection > div.modal-dialog > div > div"
    img_player_id = "btn_SelectedPlayerNormal"

    def clickContentFolderIcon(self):  # clicking content folder from dashboard
        self.driver.find_element_by_xpath(self.img_folder_xpath).click()

    def clickSelectToAdd(self):  # clicking 3lines to add
        self.driver.find_element_by_xpath(self.button_select_to_add_xpath).click()

    def clickCreateContentFolder(self):  # Clicking to Add content
        self.driver.find_element_by_id(self.button_create_folder_id).click()

    def clickPlayerType(self):
        self.driver.find_element_by_css_selector(self.img_player_css)

    def clickPlayer(self):
        self.driver.find_element_by_id(self.img_player_id).click()

