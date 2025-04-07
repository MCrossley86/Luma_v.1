# Import the necessary modules
from pageobjects.HomePage import MainPage
from pageobjects.CustomerLogin import CustLogin
from pageobjects.MyAccount import MyAccount
from pageobjects.YogaCollection import YogaCollection
from pageobjects.CompareProducts import CompareProducts
from utilities.CustomLog import LogGenerator
from utilities.ReadProperties import ReadConfig
import pytest
import os

class TestAddToCompare:
    # Get the URL, user email and password from the config file and initialize the logger
    baseURL = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGenerator.get_logger()

    @pytest.mark.sanity
    def test_add_to_comp(self, setup):
        # Log the action, define and create a path to save screenshots
        self.logger.info("*** Test_006_AddToComp started ***")
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
            self.mp = MainPage(self.driver)
            self.mp.click_sign()

            # Log the action and enter the required credentials into the corresponding fields
            self.logger.info("*** Sign into the application ***")
            self.cl = CustLogin(self.driver)
            self.cl.enter_email(self.user_email)
            self.cl.enter_pwd(self.password)
            self.cl.click_signin()

            # Log the action and click on the Yoga collection link
            self.logger.info("*** Click on the Yoga collection link ***")
            self.ma = MyAccount(self.driver)
            self.ma.click_promo_link()

            # Log the action and click on compare icons for Echo and Gwen shorts
            self.logger.info("*** Click on compare icons for Echo and Gwen shorts ***")
            self.yc = YogaCollection(self.driver)
            self.yc.click_echo_compare()
            self.yc.click_gwen_compare()
            self.yc.comparison_list_lnk()

            # Log the action and check for the header title and compared items
            self.logger.info("*** Check to see if header and items displayed ***")
            self.cp = CompareProducts(self.driver)
            self.comp_head = self.cp.compare_header()
            self.comp_gwen = self.cp.compare_gwen_short_displayed()
            self.comp_echo = self.cp.compare_echo_short_displayed()
            assert self.comp_head == "Compare Products" and self.comp_echo and self.comp_gwen
            self.driver.quit()
            self.logger.info("*** Test_006_AddToComp Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_006_AddToComp Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_add_to_comp.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_006_AddToComp Complete ***")