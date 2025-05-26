# Import the necessary modules
from pageobjects.HomePage import HomePage
from pageobjects.SearchResults import SearchResults
from utilities.ReadProperties import ReadConfig
from utilities.CustomLog import LogGenerator
import pytest
import os

class TestSearchField:
    # Get the URL from the config file and initialize the logger
    baseURL = ReadConfig.get_application_url()
    logger = LogGenerator.get_logger()

    @pytest.mark.sanity
    def test_search_field(self, setup):
        # Log the action, define and create a path to save screenshots
        self.logger.info("*** Test_010_Search_Field Started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            # Log the action and navigate to the main page
            self.logger.info("*** Navigate to the main page ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and search for a specific item
            self.logger.info("*** Clicking in the search field and searching ***")
            self.hp = HomePage(self.driver)
            self.hp.click_search_fld()
            self.hp.set_search_item("Argus")
            self.hp.select_search_item()

            # Log the action and check for the header title
            self.logger.info("*** Checking for header title ***")
            self.sr = SearchResults(self.driver)
            self.conf_title = self.sr.capture_header_txt()
            assert self.conf_title == "Search results for: 'argus'"
            self.driver.quit()
            self.logger.info("*** Test_010_Search_Field Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_010_Search_Field Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_search_field.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_010_Search_Field Complete ***")