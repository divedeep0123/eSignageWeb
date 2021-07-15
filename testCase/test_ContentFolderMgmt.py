from pageObjects.ContentFolderManagement import content

class Test_002_ContentFolderManagement:
    baseURL="http://localhost/webapp/eSignageS/login/tenant.ejs"
    username="admin"
    password="admin"

    def test_content_folder_icon(self,setup):
        self.driver=setup
        self.driver.get(baseURL)