# Import the necessary modules
from selenium.webdriver.common.by import By
from utilities.CustomLog import LogGenerator

class YogaCollection:
    # Define locators for webpage elements
    echo_lnk = "//img[@alt='Echo Fit Compression Short']"
    echo_add_to_cart = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/button[1]/span[1]"
    echo_add_to_wishlist = "//li[1]//div[1]//div[1]//div[4]//div[1]//div[2]//a[1]"
    echo_add_to_compare = "//li[1]//div[1]//div[1]//div[4]//div[1]//div[2]//a[2]"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def click_echo_link(self):
        # Log the action and click on the designated link
        self.logger.debug(f"Clicking on the echo fit image")
        self.driver.find_element(By.XPATH, self.echo_lnk).click()

    def add_echo_to_cart(self):
        # Log the action and click "add to cart" in the iframe
        self.logger.debug(f"Clicking on echo fit add to cart")
        self.driver.find_element(By.XPATH, self.echo_add_to_cart).click()

    def add_echo_to_wishlist(self):
        # Log the action and click the heart icon in the iframe
        self.logger.debug(f"Clicking on echo fit  wishlist icon")
        self.driver.find_element(By.XPATH, self.echo_add_to_wishlist).click()

    def add_echo_to_compare(self):
        # Log the action and click the bar chart icon in the iframe
        self.logger.debug(f"Clicking on echo fit compare icon")
        self.driver.find_element(By.XPATH, self.echo_add_to_compare).click()