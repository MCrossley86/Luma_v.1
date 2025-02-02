# add the following imports - AccountsRegistration, HomePage, RandomString, CustomLog ReadProperties and os
# in ReadProperties create static methods for URL. Add to config.ini
# create a class
# in Test_001 add the variables baseURL=getapplicationurl() and logger
# create method
    # launch browser, click create an account, enter details, click sign in, check for "Home Page" title
# setup screenshots to capture failures
# create a group

from pageobjects.AccountRegistration import RegPage
from pageobjects.HomePage import MainPage
from utilities.RandomString import random_string_generator
from utilities.ReadProperties import ReadConfig
from utilities.CustomLog import LogGenerator
import pytest
import os

class TestAccountReg:
    baseURL = ReadConfig.getapplicationurl()
    logger = LogGenerator.get_logger()

    @pytest.mark.sanity
    def test_account_reg(self, setup):
        self.logger.info("*** Account Registration Started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            self.logger.info("*** Navigate to Account Registration ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.logger.info("*** Click Account ***")
            self.mp=MainPage(self.driver)
            self.mp.clickaccount()

            self.logger.info("*** Enter Personal Details ***")
            self.rp=RegPage(self.driver)
            self.rp.setfirstname("Jane")
            self.rp.setlastname("Doe")
            self.email=random_string_generator()+'@gmail.com'
            self.rp.setemail(self.email)
            self.rp.setpassword("abc123DEF")
            self.rp.confirmpassword("abc123DEF")
            self.rp.clickcreate()
            self.confhead=self.rp.getheadtitle()
            assert self.confhead=="My Account"
            self.logger.info("*** Account Registration Passed ***")
        except Exception:
            self.logger.info("*** Account Registration Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_account_reg.png")
            self.driver.save_screenshot(screenshot_filename)
            raise Exception
        self.logger.info("*** Account Registration Complete ***")