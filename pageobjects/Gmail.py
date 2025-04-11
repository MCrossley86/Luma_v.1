from utilities.WaitForElements import wait_for_element
from utilities.WaitForElements import element_clickable
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utilities.CustomLog import LogGenerator

class GmailAccount:
    # Define locators for webpage elements
    user_name_fld = "//input[@id='identifierId']"
    user_pwd = "//input[@name='Passwd']"
    next_btn = "//span[normalize-space()='Next']"
    not_now_button = "//span[normalize-space()='Not now']"
    save_btn = "//span[normalize-space()='Save']"
    search_field = "//input[@placeholder='Search mail']"
    magnify_icon = "//button[@aria-label='Search mail']//*[name()='svg']"
    g_mail = "//span[normalize-space()='Recover Your Account']"
    recover_acc = "//a[normalize-space()='recover your account']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def enter_email(self, email):
        # Log the action and enter the email in the corresponding field
        self.logger.debug(f"Entering email: {email}")
        wait_for_element(self.driver, self.user_name_fld).send_keys(email)

    def enter_pwd(self, pwd):
        # Log the action and enter the password in the corresponding field
        self.logger.debug(f"Entering password: {pwd}")
        wait_for_element(self.driver, self.user_pwd).send_keys(pwd)

    def click_next(self):
        # Log the action and click the "Next" button
        self.logger.debug(f"Clicking Next")
        element_clickable(self.driver, self.next_btn).click()

    def click_not_now(self):
        # Log the action and click the "Not Now" button
        self.logger.debug(f"Clicking Not Now")
        wait_for_element(self.driver, self.not_now_button).click()

    def click_save(self):
        # Log the action and click the "Save" button
        self.logger.debug(f"Clicking Save")
        wait_for_element(self.driver, self.save_btn).click()

    def gmail_search_field(self, subject):
        # Log the action and enter "Security" in the search field
        self.logger.debug(f"Entering security in the search field")
        element_clickable(self.driver, self.search_field).send_keys(subject)

    def magnify_glass(self):
        # Log the action and click on the magnifying glass icon
        self.logger.debug(f"Clicking on the icon")
        element_clickable(self.driver, self.magnify_icon).click()

    def open_gmail(self):
        # Log the action and click on the email
        self.logger.debug(f"Clicking on the email")
        element_clickable(self.driver, self.g_mail).click()

    def recovering_account(self):
        # Log the action and click "recover your account"
        self.logger.debug(f"Recovering account")
        element_clickable(self.driver, self.recover_acc).click()
