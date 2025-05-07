# Import the necessary modules
from pageobjects.HomePage import MainPage
from pageobjects.NavBar import NavBarHP
from utilities.ReadProperties import ReadConfig
from utilities.CustomLog import LogGenerator
import os

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
            # Log the action and navigate to the account registration page
            self.logger.info("*** Navigate to the main page ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and click on what's new in the nav bar
            self.logger.info("*** Clicking what's new in the nav bar ***")
            self.mp = MainPage(self.driver)

            # Click on the nav bar links and check the headers
            self.nb = NavBarHP(self.driver)
            self.nb.click_whats_new()
            self.wn_title = self.nb.whats_new_title()
            assert self.wn_title == "What's New"
            self.nb.click_women()
            self.w_title = self.nb.women_title()
            assert self.w_title == "Women"
            self.nb.women_tops_click()
            current_url = self.driver.current_url
            w_tops_expected_url = "https://magento.softwaretestingboard.com/women/tops-women.html"
            assert current_url == w_tops_expected_url
            self.nb.women_jacket_click()
            current_url = self.driver.current_url
            w_jacket_expected_url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
            assert current_url == w_jacket_expected_url
            self.nb.women_bottoms_click()
            current_url = self.driver.current_url
            w_bottoms_expected_url = "https://magento.softwaretestingboard.com/women/bottoms-women.html"
            assert current_url == w_bottoms_expected_url
            self.nb.click_men()
            self.m_title = self.nb.men_title()
            assert self.m_title == "Men"
            self.nb.click_gear()
            self.g_title = self.nb.gear_title()
            assert self.g_title == "Gear"
            self.nb.click_training()
            self.t_title = self.nb.training_title()
            assert self.t_title == "Training"
            self.nb.click_sale()
            self.s_title = self.nb.sale_title()
            assert self.s_title == "Sale"
            self.driver.quit()
            self.logger.info("*** Test_011_Nav_Bar_Field Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_011_Nav_Bar Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_nav_bar.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_011_Nav_Bar Complete ***")