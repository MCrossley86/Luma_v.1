# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator

class MyAccount:
    # Define locators for webpage elements
    txt_conf = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='My Account']"
    lnk_my_account_xpath = "//div[@aria-hidden='false']//a[normalize-space()='My Account']"
    lnk_my_wishlist_xpath = "//div[@aria-hidden='false']//a[normalize-space()='My Wish List']"
    lnk_promo_xpath = "//span[@class='info']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def click_my_account(self):
        # Log the action and click the "My Account" link
        self.logger.debug(f"Clicking My Account link")
        wait_for_element(self.driver, self.lnk_my_account_xpath).click()

    def click_my_wishlist(self):
        # Log the action and click the "My Wishlist" link
        self.logger.debug(f"Clicking My Wishlist link")
        wait_for_element(self.driver, self.lnk_my_wishlist_xpath).click()

    def click_promo_link(self):
        # Log the action and click the "New Luma Collection" link
        self.logger.debug(f"Clicking new luma collection link")
        wait_for_element(self.driver, self.lnk_promo_xpath).click()

    def capt_ma_head(self):
        # Capture the header title text and handle any exceptions
        try:
            return wait_for_element(self.driver, self.txt_conf).text
        except Exception as e:
            self.logger.error(f"Error retrieving head title: {e}")
            return None

    def capture_url(self):
        # Capture the url
        return self.driver.current_url

