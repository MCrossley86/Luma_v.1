# Import the necessary modules
from pageobjects.HomePage import MainPage
from pageobjects.CustomerLogin import CustLogin
from pageobjects.MyAccount import MyAccount
from utilities.CustomLog import LogGenerator
from utilities.ReadProperties import ReadConfig
import pytest
import os

class TestLogout:
    # Get the URL, user email and password from the config file and initialize the logger
    baseURL = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGenerator.get_logger()

    @pytest.mark.sanity
    def test_logout(self,setup):
        # Log the action, define and create a path to save screenshots
        self.logger.info("*** Test_003_Logout Started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            # Log the action and navigate to the main page
            self.logger.info("*** Navigate to the main page ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and click the "Sign In" link
            self.logger.info("*** Click Sign In ***")
            self.mp=MainPage(self.driver)
            self.mp.click_sign()

            # Log the action and enter the required credentials into the corresponding fields
            self.logger.info("*** Sign into the application ***")
            self.cl=CustLogin(self.driver)
            self.cl.enter_email(self.user_email)
            self.cl.enter_pwd(self.password)
            self.cl.click_signin()

            # Log the action and log out via the navigation bar
            self.logger.info("*** Log out of the application ***")
            self.ma=MyAccount(self.driver)
            self.ma.click_welcome()
            self.ma.click_sign_out()

            # Log the action and check for the "signed out" message
            self.logger.info("*** Check for sign out message ***")
            self.conf_sign_out = self.ma.get_sign_out_msg()
            assert self.conf_sign_out == "You are signed out"
            self.driver.close()
            self.logger.info("*** Test_003_Logout Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_003_Logout Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_logout.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_003_Logout Complete ***")