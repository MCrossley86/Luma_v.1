# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator

class MyAccount:
    # Define locators for webpage elements
    lnk_welcome_xpath = "//div[@class='panel header']//button[@type='button']"
    lnk_my_account_xpath = "//div[@aria-hidden='false']//a[normalize-space()='My Account']"
    lnk_my_wishlist_xpath = "//div[@aria-hidden='false']//a[normalize-space()='My Wish List']"
    lnk_sign_out_xpath = "//div[@aria-hidden='false']//a[normalize-space()='Sign Out']"
    lnk_promo_xpath = "//span[@class='info']"
    sign_out_conf = "//span[@class='base']"


    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def click_welcome(self):
        # Log the action and click the "Welcome" dropdown arrow
        self.logger.debug(f"Clicking Welcome dropdown arrow")
        wait_for_element(self.driver, self.lnk_welcome_xpath).click()

    def click_my_account(self):
        # Log the action and click the "My Account" link
        self.logger.debug(f"Clicking My Account link")
        wait_for_element(self.driver, self.lnk_my_account_xpath).click()

    def click_my_wishlist(self):
        # Log the action and click the "My Wishlist" link
        self.logger.debug(f"Clicking My Wishlist link")
        wait_for_element(self.driver, self.lnk_my_wishlist_xpath).click()

    def click_sign_out(self):
        # Log the action and click the "Sign Out" link
        self.logger.debug(f"Clicking Sign Out link")
        wait_for_element(self.driver, self.lnk_sign_out_xpath).click()

    def click_promo_link(self):
        # Log the action and click the "New Luma Collection" link
        self.logger.debug(f"Clicking new luma collection link")
        wait_for_element(self.driver, self.lnk_promo_xpath).click()

    def get_sign_out_msg(self):
        # Log the action and capture the "signed out" text
        self.logger.debug(f"Capturing the signed out header text")
        try:
            return wait_for_element(self.driver, self.sign_out_conf).text
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

