from selenium.webdriver.common.by import By

class CustLogin():
    fld_email_xpth = "//input[@id='email']"
    fld_pwd_xpth = "//fieldset[@class='fieldset login']//input[@id='pass']"
    fld_sign_xpth = "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]"
    txt_conf_title = "//span[@class='base']"

    def __init__(self,driver):
        self.driver = driver

    def enteremail(self,email):
        self.driver.find_element(By.XPATH,self.fld_email_xpth).send_keys(email)

    def enterpwd(self, pwd):
        self.driver.find_element(By.XPATH,self.fld_pwd_xpth).send_keys(pwd)

    def clicksignin(self):
        self.driver.find_element(By.XPATH,self.fld_sign_xpth).click()

    def gethomepagetitle(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_conf_title).text
        except:
            None