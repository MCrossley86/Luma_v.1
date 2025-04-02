# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator

class ForgotPwd:
    # Define locators for webpage elements
    email_field = "//input[@id='email_address']"
    reset_btn = "//button[@class='action submit primary']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def enter_email(self, email):
        # Log the action and enter the email in the corresponding field
        self.logger.debug(f"Entering email: {email}")
        wait_for_element(self.driver, self.email_field).send_keys(email)

    def click_reset(self):
        # Log the action and click the "Reset My Password" button
        self.logger.debug(f"Clicking reset password button")
        wait_for_element(self.driver, self.reset_btn).click()