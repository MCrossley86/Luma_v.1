# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from selenium.webdriver import ActionChains
from utilities.CustomLog import LogGenerator

class NavBarHP:
    # Define locators for webpage elements
    whats_new_lnk = "(//a[@id='ui-id-3'])[1]"
    w_lnk = "(//a[@id='ui-id-4'])[1]"
    head_conf = "//span[@class='base']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def click_whats_new_lnk(self):
        # Log the action and click the "What's New" link
        self.logger.debug(f"Clicking the What's New link")
        wait_for_element(self.driver, self.whats_new_lnk).click()

    def click_women_lnk(self):
        # Log the action and click the "Women" link
        self.logger.debug(f"Clicking the Women link")
        wait_for_element(self.driver, self.w_lnk).click()

    def capt_header_title(self):
        # Capture the header title text and handle any exceptions
        try:
            return wait_for_element(self.driver, self.head_conf).text
        except Exception as e:
            self.logger.error(f"Error retrieving head title: {e}")
            return None

