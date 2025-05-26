# Import the necessary modules
from pageobjects.HomePage import HomePage
from pageobjects.CustomerLogin import CustLogin
from utilities.CustomLog import LogGenerator
from utilities.ReadProperties import ReadConfig
import pytest
import os

class TestLogin:
    # Get the URL, user email and password from the config file and initialize the logger
    baseURL = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGenerator.get_logger()

    @pytest.mark.sanity
    def test_login(self, setup):
        # Log the action, define and create a path to save screenshots
        self.logger.info("*** Test_002_Login Started ***")
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
            self.hp=HomePage(self.driver)
            self.hp.click_sign()

            # Log the action and enter the required credentials into the corresponding fields
            self.logger.info("*** Sign into the application ***")
            self.cl=CustLogin(self.driver)
            self.cl.enter_email(self.user_email)
            self.cl.enter_pwd(self.password)
            self.cl.click_signin()

            # Log the action and check for the header title
            self.logger.info("*** Check for header title ***")
            self.conf_title = self.cl.get_home_page_title()
            assert self.conf_title=="Home Page"
            self.driver.quit()
            self.logger.info("*** Test_002_Login Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_002_Login Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_login.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_002_Login Complete ***")
