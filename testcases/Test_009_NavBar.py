# Import the necessary modules
from pageobjects.NavBar import NavBarHP
from utilities.ReadProperties import ReadConfig
from utilities.CustomLog import LogGenerator
import pytest
import os

class TestNavBar:
    # Get the URL from the config file and initialize the logger
    baseURL = ReadConfig.get_application_url()
    logger = LogGenerator.get_logger()

    @pytest.mark.sanity
    def test_nav_bar(self, setup):
        # Log the action, define and create a path to save screenshots
        self.logger.info("*** Test_011_Nav_Bar Started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            # Log the action and import the classes from the Page Object files
            self.logger.info("*** Adding Classes from Page Object files ***")
            self.nb = NavBarHP(self.driver)


            # Log the action and open up the webpage
            self.logger.info("*** Opening the webpage ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and click on the nav bar links and check the headers
            self.logger.info("*** Checking links in the nav bar ***")
            self.nb.click_whats_new_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "What's New" and self.capt_url == "https://magento.softwaretestingboard.com/what-is-new.html"
            self.nb.click_women_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Women" and self.capt_url == "https://magento.softwaretestingboard.com/women.html"
            self.nb.click_w_tops_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Tops" and self.capt_url == "https://magento.softwaretestingboard.com/women/tops-women.html"
            self.nb.click_w_jackets_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Jackets" and self.capt_url == "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
            self.nb.click_w_hoodies_sweatshirts_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Hoodies & Sweatshirts" and self.capt_url == "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"
            self.nb.click_w_tees_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Tees" and self.capt_url == "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"
            self.nb.click_w_bras_tanks_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Bras & Tanks" and self.capt_url == "https://magento.softwaretestingboard.com/women/tops-women/tanks-women.html"
            self.nb.click_w_bottoms_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Bottoms" and self.capt_url == "https://magento.softwaretestingboard.com/women/bottoms-women.html"
            self.nb.click_w_pants_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Pants" and self.capt_url == "https://magento.softwaretestingboard.com/women/bottoms-women/pants-women.html"
            self.nb.click_w_shorts_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Shorts" and self.capt_url == "https://magento.softwaretestingboard.com/women/bottoms-women/shorts-women.html"
            self.nb.click_men_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Men" and self.capt_url == "https://magento.softwaretestingboard.com/men.html"
            self.nb.click_m_tops_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Tops" and self.capt_url == "https://magento.softwaretestingboard.com/men/tops-men.html"
            self.nb.click_m_jackets_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Jackets" and self.capt_url == "https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html"
            self.nb.click_m_hoodies_sweatshirts_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Hoodies & Sweatshirts" and self.capt_url == "https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html"
            self.nb.click_m_tees_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Tees" and self.capt_url == "https://magento.softwaretestingboard.com/men/tops-men/tees-men.html"
            self.nb.click_m_tanks_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Tanks" and self.capt_url == "https://magento.softwaretestingboard.com/men/tops-men/tanks-men.html"
            self.nb.click_m_bottoms_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Bottoms" and self.capt_url == "https://magento.softwaretestingboard.com/men/bottoms-men.html"
            self.nb.click_m_pants_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Pants" and self.capt_url == "https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html"
            self.nb.click_m_shorts_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Shorts" and self.capt_url == "https://magento.softwaretestingboard.com/men/bottoms-men/shorts-men.html"
            self.nb.click_gear_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Gear" and self.capt_url == "https://magento.softwaretestingboard.com/gear.html"
            self.nb.click_bag_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Bags" and self.capt_url == "https://magento.softwaretestingboard.com/gear/bags.html"
            self.nb.click_fit_equip_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Fitness Equipment" and self.capt_url == "https://magento.softwaretestingboard.com/gear/fitness-equipment.html"
            self.nb.click_watches_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Watches" and self.capt_url == "https://magento.softwaretestingboard.com/gear/watches.html"
            self.nb.click_training_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Training" and self.capt_url == "https://magento.softwaretestingboard.com/training.html"
            self.nb.click_vid_dwnld_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Video Download" and self.capt_url == "https://magento.softwaretestingboard.com/training/training-video.html"
            self.nb.click_sale_lnk()
            self.conf_head = self.nb.capt_header_title()
            self.capt_url = self.nb.capture_url()
            assert self.conf_head == "Sale" and self.capt_url == "https://magento.softwaretestingboard.com/sale.html"
            self.driver.quit()
            self.logger.info("*** Test_011_Nav_Bar_Field Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_011_Nav_Bar Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_nav_bar.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_011_Nav_Bar Complete ***")