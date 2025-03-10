# Import the necessary modules
from utilities.CustomLog import LogGenerator
from utilities.WaitForElements import wait_for_element

class MyWishList:
    # Define locators for webpage elements
    wish_list_head = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='My Wish List']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def wish_list_header(self):
        # Log the action and capture the "My Wish List" text
        self.logger.debug(f"Capturing the My Wish List header text")
        try:
            return wait_for_element(self.driver, self.wish_list_head).text
        except Exception as e:
            print(f"An error occurred: {e}")
            return False