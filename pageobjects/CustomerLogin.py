from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class CustLogin:
    fld_email_xpth = "//input[@id='email']"
    fld_pwd_xpth = "//fieldset[@class='fieldset login']//input[@id='pass']"
    fld_sign_xpth = "//fieldset[@class='fieldset login']//button[@id='send2']"
    txt_conf_title = "//span[@class='base']"
    msg_myaccount_xpath = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='Home Page']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enteremail(self,email):
        print(f"Current URL: {self.driver.current_url}")
        print("Enter email")
        email_field = self.wait.until(
            ec.presence_of_element_located((By.XPATH, self.fld_email_xpth))
        )
        email_field.clear()
        email_field.send_keys(email)

    def enterpwd(self, pwd):
        print(f"Current URL: {self.driver.current_url}")
        print("Enter password")
        pwd_field = self.wait.until(
            ec.presence_of_element_located((By.XPATH, self.fld_pwd_xpth))
        )
        pwd_field.clear()  # Clear any existing text
        pwd_field.send_keys(pwd)

    def clicksignin(self):
        print(f"Current URL: {self.driver.current_url}")
        print("Click signin")
        signin_button = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, self.fld_sign_xpth))
        )
        signin_button.click()

    def clear_email_field(self):
        print(f"Current URL: {self.driver.current_url}")
        print("Clear email field")
        self.driver.find_element(By.XPATH, self.fld_email_xpth).clear()

    def clear_password_field(self):
        print(f"Current URL: {self.driver.current_url}")
        print("Clear password field")
        self.driver.find_element(By.XPATH, self.fld_pwd_xpth).clear()

    def gethomepagetitle(self):
        print(f"Current URL: {self.driver.current_url}")
        print("Capturing text")
        try:
            text_capture = self.driver.find_element(By.XPATH, self.txt_conf_title).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def ismyaccountpageexists(self):
        print(f"Current URL: {self.driver.current_url}")
        print("Checking for element")
        try:
            element_displayed = self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
            print("Element displayed...")
            return element_displayed
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
