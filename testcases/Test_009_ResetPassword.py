# Import the necessary modules
from pageobjects.HomePage import MainPage
from pageobjects.CustomerLogin import CustLogin
from pageobjects.ForgotYourPassword import ForgotPwd
from pageobjects.Gmail import GmailAccount
from utilities.CustomLog import LogGenerator
from utilities.ReadProperties import ReadConfig
import pytest
import os
import time

class TestResetPwd:
    # Get the URL, user email and password from the config file and initialize the logger
    baseURL = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGenerator.get_logger()
    imap_url = "imap.gmail.com"

    # @pytest.mark.sanity
    def test_login(self, setup):
        # Log the action, define and create a path to save screenshots
        self.logger.info("*** Test_009_ResetPassword Started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            # Log the action and navigate to the main page
            self.logger.info("*** Navigate to the main page ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and click the "Sign In" link
            self.logger.info("*** Click Sign In ***")
            self.mp=MainPage(self.driver)
            self.mp.click_sign()

            # Log the action and click "Forgot Your Password"
            self.logger.info("*** Click Forgot Your Password ***")
            self.cl = CustLogin(self.driver)
            self.cl.click_forgot_pwd()

            # Log the action and reset the password
            self.logger.info("*** Resetting the password ***")
            self.fp = ForgotPwd(self.driver)
            self.fp.enter_email(self.user_email)
            self.fp.click_reset()

            # Log the action and check for the green confirmation bar
            self.logger.info("*** Check for the confirmation bar ***")
            assert self.cl.pwd_reset_conf()

            # Open Gmail and check for the link
            self.logger.info("*** Check for the email link ***")
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get("https://mail.google.com")
            self.ga = GmailAccount(self.driver)
            self.ga.enter_email(self.user_email)
            self.ga.click_next()
            self.ga.enter_pwd(self.password)
            self.ga.click_next()
            time.sleep(2)

            # Search for the email
            # self.ga.gmail_search_field()
            self.ga.set_subject_name("Security Alert")
            self.ga.magnify_glass()
            time.sleep(5)
            #
            # # Open the email
            self.ga.open_gmail()
            # time.sleep(5)

            # # Find and click the password reset link
            # reset_link = self.driver.find_element(By.XPATH, "//a[contains(text(), 'recover your account')]")
            # ActionChains(self.driver).move_to_element(reset_link).click().perform()
            self.driver.quit()
            self.logger.info("*** Test_009_ResetPassword Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_009_ResetPassword Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_reset_pwd.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_009_ResetPassword Complete ***")