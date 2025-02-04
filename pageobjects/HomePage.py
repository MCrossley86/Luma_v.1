from selenium.webdriver.common.by import By

class MainPage:
    lnk_account_xpth = "//div[@class='panel header']//a[normalize-space()='Create an Account']"
    lnk_sign_xpth = "//div[@class='panel header']//a[contains(text(),'Sign In')]"

    def __init__(self, driver):
         self.driver = driver

    def clickaccount(self):
        self.driver.find_element(By.XPATH,self.lnk_account_xpth).click()

    def clicksign(self):
        self.driver.find_element(By.XPATH,self.lnk_sign_xpth).click()