# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator

class SearchResults:
    # Define locators for webpage elements
    txt_conf_title = "//span[@class='base']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def capture_header_txt(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = wait_for_element(self.driver, self.txt_conf_title).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False