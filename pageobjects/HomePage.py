# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from selenium.webdriver import ActionChains
from utilities.CustomLog import LogGenerator

class HomePage:
    # Define locators for webpage elements
    hme_pge_head = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='Home Page']"
    lnk_sign_xpath = "//div[@class='panel header']//a[contains(text(),'Sign In')]"
    lnk_account_xpath = "//div[@class='panel header']//a[normalize-space()='Create an Account']"
    sign_out_conf = "//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='You are signed out']"
    luma_yoga_xpath = "//span[@class='info']"
    search_fld = "//input[@id='search']"
    hover_dropdown = "(//li[@id='qs-option-0'])[1]"
    click_dropdown = "(//li[@id='qs-option-1'])[1]"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def capt_hp_head(self):
        # Capture the header title text and handle any exceptions
        try:
            return wait_for_element(self.driver, self.hme_pge_head).text
        except Exception as e:
            self.logger.error(f"Error retrieving head title: {e}")
            return None

    def click_sign_in_lnk(self):
        # Log the action and click the "Sign In" link
        self.logger.debug(f"Clicking Sign in link")
        wait_for_element(self.driver, self.lnk_sign_xpath).click()

    def click_create_account(self):
        # Log the action and click the "Create an Account" link
        self.logger.debug(f"Clicking create an account link")
        wait_for_element(self.driver, self.lnk_account_xpath).click()

    def capt_so_head(self):
        # Log the action and capture the "signed out" text
        self.logger.debug(f"Capturing the signed out header text")
        try:
            return wait_for_element(self.driver, self.sign_out_conf).text
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def capture_url(self):
        # Capture the url
        return self.driver.current_url

    def click_luma_yoga_link(self):
        # Log the action and click the "New Luma Collection" link
        self.logger.debug(f"Clicking new luma collection link")
        wait_for_element(self.driver, self.luma_yoga_xpath).click()

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