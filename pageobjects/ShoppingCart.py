# Import the necessary modules
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator

class ShoppingCart:
    # Define locators for webpage elements
    shop_cart_head = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='Shopping Cart']"
    shop_cart_item = "//td[@class='col item']//a[normalize-space()='Echo Fit Compression Short']"
    shop_cart_item_tank = "//td[@class='col item']//a[normalize-space()='Cassius Sparring Tank']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    # def wait_for_element(self, locator):
    #     # Method to wait for element before any action is committed
    #     self.logger.debug(f"Waiting for the element with locator: {locator}")
    #     return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, locator))
    #         )

    def capt_head_title(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = wait_for_element(self.driver, self.shop_cart_head).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def capt_added_item(self):
        # Log the action and check the header is displayed
        self.logger.debug(f"Checking item has been added")
        try:
            element_displayed = wait_for_element(self.driver, self.shop_cart_item).is_displayed()
            print("Item added...")
            return element_displayed
        except Exception as e:
            print(f"An error occurred: {e}")
            return False