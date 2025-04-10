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
    search_field = "(//div[@id='gs_lc50'])[1]"
    magnify_icon = "//button[@aria-label='Search mail']//*[name()='svg']"

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
        wait_for_element(self.driver, self.next_btn).click()

    def click_not_now(self):
        # Log the action and click the "Not Now" button
        self.logger.debug(f"Clicking Not Now")
        wait_for_element(self.driver, self.not_now_button).click()

    def click_save(self):
        # Log the action and click the "Save" button
        self.logger.debug(f"Clicking Save")
        wait_for_element(self.driver, self.save_btn).click()

    def gmail_search_field(self):
        wait_for_element(self.driver, self.save_btn).click()

    def set_subject_name(self, subject):
        self.driver.find_element(By.NAME, "q").send_keys(subject)

    def magnify_glass(self):
        element_clickable(self.driver, self.magnify_icon).click()

    def open_gmail(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Security')]").click()
