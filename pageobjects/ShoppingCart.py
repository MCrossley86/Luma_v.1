# Import the necessary modules
from selenium.webdriver.common.by import By
from utilities.CustomLog import LogGenerator

class ShoppingCart:
    # Define locators for webpage elements
    shop_cart_head = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='Shopping Cart']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def capt_head_title(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = self.driver.find_element(By.XPATH, self.shop_cart_head).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
