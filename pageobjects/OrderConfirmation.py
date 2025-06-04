# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator

class OrderConf:
    # Define locators for webpage elements
    order_conf = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='Thank you for your purchase!']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def order_conf_head(self):
        # Log the action and capture the "Purchase" text
        self.logger.debug(f"Capturing the purchase header text")
        try:
            return wait_for_element(self.driver, self.order_conf).text
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def capture_url(self):
        # Capture the url
        return self.driver.current_url