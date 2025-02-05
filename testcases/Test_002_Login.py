from pageobjects.HomePage import MainPage
from pageobjects.CustomerLogin import CustLogin
from utilities.CustomLog import LogGenerator
from utilities.ReadProperties import ReadConfig
import pytest
import os

class TestLogin:
    baseURL = ReadConfig.getapplicationurl()
    useremail = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    logger = LogGenerator.get_logger()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("*** Test_002_Login Started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.logger.info("*** Click Sign In ***")
            self.mp=MainPage(self.driver)
            self.mp.clicksign()

            self.logger.info("*** Enter Credentials ***")
            self.cl=CustLogin(self.driver)
            self.cl.enteremail(self.useremail)
            self.cl.enterpwd(self.password)
            self.cl.clicksignin()

            self.logger.info("*** Check Header ***")
            self.conftitle = self.cl.gethomepagetitle()
            assert self.conftitle=="Home Page"
            self.logger.info("*** Login Passed ***")
        except Exception:
            self.logger.info("*** Login Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_login.png")
            self.driver.save_screenshot(screenshot_filename)
            raise Exception
        self.logger.info("*** Test_002_Login Complete ***")
