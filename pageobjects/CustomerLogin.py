from selenium.webdriver.common.by import By

class CustLogin():
    fld_email_xpth = "//input[@id='email']"
    fld_pwd_xpth = "//fieldset[@class='fieldset login']//input[@id='pass']"

    def __init__(self,driver):
        self.driver = driver

    def enteremail(self,email):
        self.driver.find_element(By.XPATH,self.fld_email_xpth).send_keys(email)

    def enterpwd(self, pwd):
        self.driver.find_element(By.XPATH,self.fld_pwd_xpth).send_keys(pwd)