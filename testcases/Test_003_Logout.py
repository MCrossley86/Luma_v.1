from pageobjects.AccountRegistration import RegPage
from pageobjects.HomePage import MainPage
from pageobjects.CustomerLogin import CustLogin
from pageobjects.MyAccount import MyAccount
from utilities.CustomLog import LogGenerator
from utilities.ReadProperties import ReadConfig
import pytest
import os
import time

class TestLogout():
    baseURL = ReadConfig.getapplicationurl()
    useremail = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    logger = LogGenerator.get_logger()

    def test_logout(self,setup):
        self.logger.info("*** Test_003_Logout Started ***")
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

            self.logger.info("*** Logout ***")
            self.ma=MyAccount(self.driver)
            self.ma.clickwelcome()
            self.ma.clicksignout()

            self.logger.info("*** Check Signout ***")
            self.confsignout = self.ma.getsignoutmsg()
            assert self.confsignout == "You are signed out"
            self.logger.info("*** Login Passed ***")
        except Exception:
            self.logger.info("*** Login Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_logout.png")
            self.driver.save_screenshot(screenshot_filename)
            raise Exception
        self.logger.info("*** Test_003_Logout Complete ***")