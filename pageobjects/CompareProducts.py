# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator

class CompareProducts:
    # Define locators for webpage elements
    comp_head = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='Compare Products']"
    comp_gwen = "//a[normalize-space()='Gwen Drawstring Bike Short']"
    comp_echo = "//a[@title='Echo Fit Compression Short'][normalize-space()='Echo Fit Compression Short']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def compare_header(self):
        # Log the action and capture the "Compare Products" text
        self.logger.debug(f"Capturing the Compare Products header text")
        try:
            return wait_for_element(self.driver, self.comp_head).text
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def compare_gwen_short_displayed(self):
        # Log the action and check if the item is displayed
        self.logger.debug(f"Checking if the item is displayed")
        try:
            element_displayed = wait_for_element(self.driver, self.comp_gwen).is_displayed()
            print("Element displayed...")
            return element_displayed
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def compare_echo_short_displayed(self):
        # Log the action and check if the item is displayed
        self.logger.debug(f"Checking if the item is displayed")
        try:
            element_displayed = wait_for_element(self.driver, self.comp_echo).is_displayed()
            print("Element displayed...")
            return element_displayed
        except Exception as e:
            print(f"An error occurred: {e}")
            return False