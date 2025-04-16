# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from selenium.webdriver import ActionChains
from utilities.CustomLog import LogGenerator

class MainPage:
    # Define locators for webpage elements
    lnk_account_xpath = "//div[@class='panel header']//a[normalize-space()='Create an Account']"
    lnk_sign_xpath = "//div[@class='panel header']//a[contains(text(),'Sign In')]"
    search_fld = "//input[@id='search']"
    hover_dropdown = "(//li[@id='qs-option-0'])[1]"
    click_dropdown = "(//li[@id='qs-option-1'])[1]"


    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def click_account(self):
        # Log the action and click the "Create an Account" link
        self.logger.debug(f"Clicking create an account link")
        wait_for_element(self.driver, self.lnk_account_xpath).click()

    def click_sign(self):
        # Log the action and click the "Sign In" link
        self.logger.debug(f"Clicking Sign in link")
        wait_for_element(self.driver, self.lnk_sign_xpath).click()

    def click_search_fld(self):
        # Log the action and click in the search field
        self.logger.debug(f"Clicking in the search field")
        wait_for_element(self.driver, self.search_fld).click()

    def set_search_item(self, argus_item):
        # Log the action and search for an item in the corresponding field
        self.logger.debug(f"Searching for an item: {argus_item}")
        wait_for_element(self.driver, self.search_fld).send_keys(argus_item)

    def select_search_item(self):
        # Log the action and click on "add to compare" icon
        self.logger.debug(f"Clicking on add to compare icon")
        act = ActionChains(self.driver)
        hover_element = wait_for_element(self.driver, self.hover_dropdown)
        comp_element = wait_for_element(self.driver, self.click_dropdown)
        act.move_to_element(hover_element).move_to_element(comp_element).click().perform()