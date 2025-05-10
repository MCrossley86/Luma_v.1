# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from selenium.webdriver import ActionChains
from utilities.CustomLog import LogGenerator

class NavBarHP:
    # Define locators for webpage elements


    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

