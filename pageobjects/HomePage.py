from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    lnk_account_xpth = "//div[@class='panel header']//a[normalize-space()='Create an Account']"
    lnk_sign_xpth = "//div[@class='panel header']//a[contains(text(),'Sign In')]"

    def __init__(self, driver):
         self.driver = driver
         self.wait = WebDriverWait(self.driver, 10)

    def clickaccount(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_account_xpth)))
        element.click()

    def clicksign(self):
        print(f"Current URL: {self.driver.current_url}")
        print("Looking for Sign In link...")
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_sign_xpth)))
        element.click()
        print("Found Sign In link, clicking...")