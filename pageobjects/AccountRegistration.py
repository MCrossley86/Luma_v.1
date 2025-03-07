# Import the necessary modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.CustomLog import LogGenerator

class RegPage:
    # Define locators for webpage elements
    txt_field_firstname = "//input[@id='firstname']"
    txt_field_lastname = "//input[@id='lastname']"
    txt_field_email = "//input[@id='email_address']"
    txt_field_password = "//input[@id='password']"
    txt_field_confirm = "//input[@id='password-confirmation']"
    btn_create = "//button[@title='Create an Account']"
    txt_conf = "//span[@class='base']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def wait_for_element(self, locator):
        # Method to wait for element before any action is committed
        self.logger.debug(f"Waiting for the element with locator: {locator}")
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, locator))
            )

    def set_first_name(self,f_name):
        # Log the action and set up the first name in the corresponding field
        self.logger.debug(f"Setting first name: {f_name}")
        self.wait_for_element(self.txt_field_firstname).send_keys(f_name)

    def set_last_name(self,l_name):
        # Log the action and set up the last name in the corresponding field
        self.logger.debug(f"Setting last name: {l_name}")
        self.wait_for_element(self.txt_field_lastname).send_keys(l_name)

    def set_email(self,email):
        # Log the action and set up the email in the corresponding field
        self.logger.debug(f"Setting email: {email}")
        self.wait_for_element(self.txt_field_email).send_keys(email)

    def set_password(self,password):
        # Log the action and set up the password in the corresponding field
        self.logger.debug(f"Setting password")
        self.wait_for_element(self.txt_field_password).send_keys(password)

    def confirm_password(self,confirm_password):
        # Log the action and confirm the password in the corresponding field
        self.logger.debug(f"Confirming password")
        self.wait_for_element(self.txt_field_confirm).send_keys(confirm_password)

    def click_create(self):
        # Log the action and click the "Create an Account" button
        self.logger.debug(f"Clicking create an account")
        self.wait_for_element(self.btn_create).click()

    def capt_header_title(self):
        # Capture the header title text and handle any exceptions
        try:
            return self.wait_for_element(self.txt_conf).text
        except Exception as e:
            self.logger.error(f"Error retrieving head title: {e}")
            return None


