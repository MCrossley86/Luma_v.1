# Import the necessary modules
from selenium.webdriver.common.by import By
from utilities.CustomLog import LogGenerator

class MainPage:
    # Define locators for webpage elements
    lnk_account_xpath = "//div[@class='panel header']//a[normalize-space()='Create an Account']"
    lnk_sign_xpath = "//div[@class='panel header']//a[contains(text(),'Sign In')]"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def click_account(self):
        # Log the action and click the "Create an Account" link
        self.logger.debug(f"Clicking create an account link")
        self.driver.find_element(By.XPATH,self.lnk_account_xpath).click()

    def click_sign(self):
        # Log the action and click the "Sign In" link
        self.logger.debug(f"Clicking Sign in link")
        self.driver.find_element(By.XPATH,self.lnk_sign_xpath).click()