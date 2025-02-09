from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustLogin():
    fld_email_xpth = "//input[@id='email']"
    fld_pwd_xpth = "//fieldset[@class='fieldset login']//input[@id='pass']"
    fld_sign_xpth = "//fieldset[@class='fieldset login']//button[@id='send2']"
    txt_conf_title = "//span[@class='base']"
    msg_myaccount_xpath = "//span[@class='base']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enteremail(self,email):
        print(f"Current URL: {self.driver.current_url}")
        print("Looking for email field...")
        email_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.fld_email_xpth))
        )
        email_field.clear()
        email_field.send_keys(email)
        print("Found email field, entering keys...")

    def enterpwd(self, pwd):
        print(f"Current URL: {self.driver.current_url}")
        print("Looking for password field...")
        pwd_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.fld_pwd_xpth))
        )
        pwd_field.clear()  # Clear any existing text
        pwd_field.send_keys(pwd)
        print("Found password field, entering keys...")

    def clicksignin(self):
        print(f"Current URL: {self.driver.current_url}")
        print("Looking for Sign In link...")
        signin_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.fld_sign_xpth))
        )
        signin_button.click()
        print("Found Sign In link, clicking...")

    def gethomepagetitle(self):
        print(f"Current URL: {self.driver.current_url}")
        print("Looking for home page title...")
        try:
            return self.driver.find_element(By.XPATH,self.txt_conf_title).text
            print("Found home page title, logging out...")
        except:
            None
        print("Found home page title, logging out...")

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
        except:
            return False