# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from utilities.CustomLog import LogGenerator


class CustLogin:
    # Define locators for webpage elements
    fld_email_xpath = "//input[@id='email']"
    fld_pwd_xpath = "//fieldset[@class='fieldset login']//input[@id='pass']"
    fld_sign_xpath = "//fieldset[@class='fieldset login']//button[@id='send2']"
    fld_forgot = "(//span[contains(text(),'Forgot Your Password?')])[1]"
    txt_conf_title = "//span[@class='base']"
    msg_my_account_xpath = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='Home Page']"
    msg_reset_pwd = "//div[@class='message-success success message']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def enter_email(self, email):
        # Log the action and enter the email in the corresponding field
        self.logger.debug(f"Entering email: {email}")
        wait_for_element(self.driver, self.fld_email_xpath).send_keys(email)

    def enter_pwd(self, pwd):
        # Log the action and enter the password in the corresponding field
        self.logger.debug(f"Entering password: {pwd}")
        wait_for_element(self.driver, self.fld_pwd_xpath).send_keys(pwd)

    def click_signin(self):
        # Log the action and click the "Sign in" button
        self.logger.debug(f"Clicking sign in")
        wait_for_element(self.driver, self.fld_sign_xpath).click()

    def click_forgot_pwd(self):
        self.logger.debug(f"Clicking Forgot Password")
        wait_for_element(self.driver, self.fld_forgot).click()

    def clear_email_field(self):
        # Log the action and clear the email field
        self.logger.debug(f"Clearing email")
        wait_for_element(self.driver, self.fld_email_xpath).clear()

    def clear_password_field(self):
        # Log the action and clear the password field
        self.logger.debug(f"Clearing password")
        wait_for_element(self.driver, self.fld_pwd_xpath).clear()

    def get_home_page_title(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = wait_for_element(self.driver, self.txt_conf_title).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def is_my_account_page_exists(self):
        # Log the action and check the header is displayed
        self.logger.debug(f"Checking header is displayed")
        try:
            element_displayed = wait_for_element(self.driver, self.msg_my_account_xpath).is_displayed()
            print("Element displayed...")
            return element_displayed
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def pwd_reset_conf(self):
        # Log the action and check the password reset message is displayed
        self.logger.debug(f"Checking the message is displayed")
        try:
            element_displayed = wait_for_element(self.driver, self.msg_reset_pwd).is_displayed()
            print("Element displayed...")
            return element_displayed
        except Exception as e:
            print(f"An error occurred: {e}")
            return False


