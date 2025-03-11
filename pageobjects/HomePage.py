# Import the necessary modules
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator

class MainPage:
    # Define locators for webpage elements
    lnk_account_xpath = "//div[@class='panel header']//a[normalize-space()='Create an Account']"
    lnk_sign_xpath = "//div[@class='panel header']//a[contains(text(),'Sign In')]"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    # def wait_for_element(self, locator):
    #     # Method to wait for element before any action is committed
    #     self.logger.debug(f"Waiting for the element with locator: {locator}")
    #     return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, locator))
    #         )

    def click_account(self):
        # Log the action and click the "Create an Account" link
        self.logger.debug(f"Clicking create an account link")
        wait_for_element(self.driver, self.lnk_account_xpath).click()

    def click_sign(self):
        # Log the action and click the "Sign In" link
        self.logger.debug(f"Clicking Sign in link")
        wait_for_element(self.driver, self.lnk_sign_xpath).click()