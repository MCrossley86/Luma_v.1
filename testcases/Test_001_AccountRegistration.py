# Import the necessary modules
from pageobjects.HomePage import HomePage
from pageobjects.AccountRegistration import RegPage
from pageobjects.MyAccount import MyAccount
from utilities.RandomString import random_string_generator
from utilities.ReadProperties import ReadConfig
from utilities.CustomLog import LogGenerator
import pytest
import os

class TestAccountReg:
    # Get the URL from the config file and initialize the logger
    baseURL = ReadConfig.get_application_url()
    logger = LogGenerator.get_logger()

    @pytest.mark.sanity
    def test_account_reg(self, setup):
        # Log the action, define and create a path to save screenshots
        self.logger.info("*** Test_001_Account_Registration Started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            # Log the action and import the classes from the Page Object files
            self.logger.info("*** Adding Classes from Page Object files ***")
            self.hp = HomePage(self.driver)
            self.rp = RegPage(self.driver)
            self.ma = MyAccount(self.driver)

            # Log the action and navigate to the account registration page
            self.logger.info("*** Navigate to the main page ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and click the create an account link
            self.logger.info("*** Click Create an Account link ***")
            self.hp.click_create_account()

            # Log the action and enter the required credentials into the corresponding fields
            self.logger.info("*** Enter required credentials and create ***")
            self.rp.set_first_name("Jane")
            self.rp.set_last_name("Doe")
            self.email = random_string_generator()+'@gmail.com'
            self.rp.set_email(self.email)
            self.rp.set_password("abc123DEF")
            self.rp.confirm_password("abc123DEF")
            self.rp.click_create_btn()

            # Log the action and check for the header title and URL
            self.logger.info("*** Check for header title and URL ***")
            self.ma_head=self.ma.capt_ma_head()
            self.capt_url = self.ma.capture_url()
            assert self.ma_head == "My Account" and self.capt_url == "https://magento.softwaretestingboard.com/customer/account/"
            self.driver.quit()
            self.logger.info("*** Test_001_Account_Registration Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_001_Account_Registration Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_account_reg.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_001_Account_Registration Complete ***")