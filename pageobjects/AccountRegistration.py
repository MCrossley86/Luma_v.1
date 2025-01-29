from selenium.webdriver.common.by import By

class RegPage():
    txt_field_firstname = "//input[@id='firstname']"
    txt_field_lastname = "//input[@id='lastname']"
    txt_field_email = "//input[@id='email_address']"
    txt_field_password = "//input[@id='password']"
    txt_field_confirm = "//input[@id='password-confirmation']"
    btn_create = "//button[@title='Create an Account']"
    txt_conf = "//span[@class='base']"

    def __init__(self, driver):
        self.driver = driver

    def setfirstname(self,fname):
        self.driver.find_element(By.XPATH,self.txt_field_firstname).send_keys(fname)

    def setlastname(self,lname):
        self.driver.find_element(By.XPATH,self.txt_field_lastname).send_keys(lname)

    def setemail(self,email):
        self.driver.find_element(By.XPATH,self.txt_field_email).send_keys(email)

    def setpassword(self,pswd):
        self.driver.find_element(By.XPATH,self.txt_field_password).send_keys(pswd)

    def confirmpassword(self,conf_pswd):
        self.driver.find_element(By.XPATH,self.txt_field_confirm).send_keys(conf_pswd)

    def clickcreate(self):
        self.driver.find_element(By.XPATH,self.btn_create).click()

    def getheadtitle(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_conf).text
        except:
            None


