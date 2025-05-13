# Import the necessary modules
from pageobjects.NavBar import NavBarHP
from utilities.ReadProperties import ReadConfig
from utilities.CustomLog import LogGenerator
import os
import time

class TestNavBar:
    # Get the URL from the config file and initialize the logger
    baseURL = ReadConfig.get_application_url()
    logger = LogGenerator.get_logger()


    def test_nav_bar(self, setup):
        # Log the action, define and create a path to save screenshots
        self.logger.info("*** Test_011_Nav_Bar Started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            # Log the action and open up the webpage
            self.logger.info("*** Opening the webpage ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and click on the nav bar links and check the headers
            self.logger.info("*** Checking links in the nav bar ***")
            self.nb = NavBarHP(self.driver)
            self.nb.click_whats_new_lnk()
            self.conf_head = self.nb.capt_header_title()
            assert self.conf_head == "What's New"
            self.nb.click_women_lnk()
            self.conf_head = self.nb.capt_header_title()
            assert self.conf_head == "Women"
            self.driver.quit()
            self.logger.info("*** Test_011_Nav_Bar_Field Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_011_Nav_Bar Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_nav_bar.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_011_Nav_Bar Complete ***")