# Import the necessary modules
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator

class CompareProducts:
    # Define locators for webpage elements
    comp_head = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='Compare Products']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    # def wait_for_element(self, locator):
    #     # Method to wait for element before any action is committed
    #     self.logger.debug(f"Waiting for the element with locator: {locator}")
    #     return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, locator))
    #         )

    def compare_header(self):
        # Log the action and capture the "Compare Products" text
        self.logger.debug(f"Capturing the Compare Products header text")
        try:
            return wait_for_element(self.driver, self.comp_head).text
        except Exception as e:
            print(f"An error occurred: {e}")
            return False