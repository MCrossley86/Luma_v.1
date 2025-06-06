# Import the necessary modules
from pageobjects.HomePage import HomePage
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
        self.logger.info("*** Test_004_AddToComp started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            # Log the action and import the classes from the Page Object files
            self.logger.info("*** Adding Classes from Page Object files ***")
            self.hp = HomePage(self.driver)
            self.yc = YogaCollection(self.driver)
            self.cp = CompareProducts(self.driver)

            # Log the action and navigate to the main page
            self.logger.info("*** Navigate to the main page ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and click on the Yoga collection link
            self.logger.info("*** Click on the Yoga collection link ***")
            self.hp.click_luma_yoga_link()

            # Log the action and click on compare icons for Echo and Gwen shorts
            self.logger.info("*** Click on compare icons for Echo and Gwen shorts ***")
            self.yc.click_echo_compare()
            self.yc.click_gwen_compare()
            self.yc.comparison_list_lnk()

            # Log the action and check that the user has been navigated to the right page and the items have been added
            self.logger.info("*** Check to see if navigated to the right page and items displayed ***")
            self.comp_head = self.cp.compare_header()
            self.comp_gwen = self.cp.compare_gwen_short_displayed()
            self.comp_echo = self.cp.compare_echo_short_displayed()
            self.capt_url = self.cp.capture_url()
            assert self.comp_head == "Compare Products" and self.comp_echo and self.comp_gwen and self.capt_url.startswith ("https://magento.softwaretestingboard.com/catalog/product_compare")

            # Log the action and remove the items from the Compare list
            self.logger.info("*** Removing items from compare list ***")
            self.cp.echo_click_x()
            self.cp.click_ok()
            self.cp.gwen_click_x()
            self.cp.click_ok()
            self.driver.quit()
            self.logger.info("*** Test_004_AddToComp Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_004_AddToComp Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_add_to_comp.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_004_AddToComp Complete ***")