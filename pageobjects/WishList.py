# Import the necessary modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.CustomLog import LogGenerator

class MyWishList:
    # Define locators for webpage elements
    wish_list_head = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='My Wish List']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def wait_for_element(self, locator):
        # Method to wait for element before any action is committed
        self.logger.debug(f"Waiting for the element with locator: {locator}")
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, locator))
            )

    def wish_list_header(self):
        # Log the action and capture the "My Wish List" text
        self.logger.debug(f"Capturing the My Wish List header text")
        try:
            return self.wait_for_element(self.wish_list_head).text
            # return self.driver.find_element(By.XPATH, self.wish_list_head).text
        except Exception as e:
            print(f"An error occurred: {e}")
            return False