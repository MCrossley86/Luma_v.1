from selenium.webdriver.common.by import By

class MyAccount:
    lnk_welcome_xpth = "//div[@class='panel header']//button[@type='button']"
    lnk_myaccount_xpth = "//div[@aria-hidden='false']//a[normalize-space()='My Account']"
    lnk_mywishlist_xpth = "//div[@aria-hidden='false']//a[normalize-space()='My Wish List']"
    lnk_signout_xpth = "//div[@aria-hidden='false']//a[normalize-space()='Sign Out']"
    signout_conf = "//span[@class='base']"

    def __init__(self, driver):
        self.driver = driver

    def clickwelcome(self):
        self.driver.find_element(By.XPATH,self.lnk_welcome_xpth).click()

    def clickmyaccount(self):
        self.driver.find_element(By.XPATH,self.lnk_myaccount_xpth).click()

    def clickmywishlist(self):
        self.driver.find_element(By.XPATH,self.lnk_mywishlist_xpth).click()

    def clicksignout(self):
        self.driver.find_element(By.XPATH,self.lnk_signout_xpth).click()

    def getsignoutmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.signout_conf).text
        except:
            None

