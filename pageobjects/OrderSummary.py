# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator

class OrderSum:
    # Define locators for webpage elements
    ship_method = "//input[@type='radio' and @value='flatrate_flatrate']"
    nxt_btn = "//button[@class='button action continue primary']"
    order_btn = "(//button[@title='Place Order'])[1]"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def slct_ship_mthd(self):
        # Log the action and click the "$5" radio button
        self.logger.debug(f"Clicking $5 radio button")
        wait_for_element(self.driver, self.ship_method).click()

    def scroll_to_bottom(self):
        # Log the action and scroll to the bottom of the page
        self.logger.debug(f"scrolling to the bottom of the page")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def clck_nxt(self):
        # Log the action and click the "Next" button
        self.logger.debug(f"Clicking Next button")
        wait_for_element(self.driver, self.nxt_btn).click()

    def clck_order(self):
        # Log the action and click the "Order" button
        self.logger.debug(f"Clicking Order button")
        wait_for_element(self.driver, self.order_btn).click()



