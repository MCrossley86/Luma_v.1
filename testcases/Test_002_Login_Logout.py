# Import the necessary modules
from pageobjects.HomePage import HomePage
from pageobjects.CustomerLogin import CustLogin
from pageobjects.NavBar import NavBarHP
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
        self.logger.info("*** Test_002_Login_Logout Started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            # Log the action and import the classes from the Page Object files
            self.logger.info("*** Adding Classes from Page Object files ***")
            self.hp = HomePage(self.driver)
            self.cl = CustLogin(self.driver)
            self.nb = NavBarHP(self.driver)

            # Log the action and navigate to the main page
            self.logger.info("*** Navigate to the main page ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and click the "Sign In" link
            self.logger.info("*** Click Sign In ***")
            self.hp.click_sign_in_lnk()

            # Log the action and check for the header title
            self.logger.info("*** Check for header title ***")
            self.cl_head = self.cl.capt_cl_head()
            assert self.cl_head == "Customer Login"

            # Log the action and enter the required credentials into the corresponding fields
            self.logger.info("*** Entering the required credentials ***")
            self.cl.enter_email(self.user_email)
            self.cl.enter_pwd(self.password)
            self.cl.click_sign_in_btn()

            # Log the action and check that the user has been navigated to the right page
            self.logger.info("*** Check for header title ***")
            self.hp_head = self.hp.capt_hp_head()
            self.capt_url = self.hp.capture_url()
            assert self.hp_head == "Home Page" and self.capt_url == "https://magento.softwaretestingboard.com/"

            # Log the action and log out via the navigation bar
            self.logger.info("*** Log out of the application ***")
            self.nb.click_welcome_drop()
            self.nb.click_sign_out()

            # Log the action and check that the user has been navigated to the right page
            self.logger.info("*** Check for header title and URL ***")
            self.so_head = self.hp.capt_so_head()
            self.capt_url = self.hp.capture_url()
            assert self.so_head == "You are signed out" and self.capt_url == "https://magento.softwaretestingboard.com/customer/account/logoutSuccess/"
            self.driver.quit()
            self.logger.info("*** Test_002_Login_Logout Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_002_Login_Logout Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_login_logout.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_002_Login_Logout Complete ***")
