# Import the necessary modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from utilities.CustomLog import LogGenerator

class YogaCollection:
    # Define locators for webpage elements
    echo_lnk = "//a[@class='product photo product-item-photo']//img[@alt='Echo Fit Compression Short']"
    comparison_lnk = "//a[normalize-space()='comparison list']"
    echo_add_to_cart = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/button[1]/span[1]"
    echo_add_to_wishlist = "//li[1]//div[1]//div[1]//div[4]//div[1]//div[2]//a[1]"
    echo_hover = "//body/div[@class='page-wrapper']/main[@id='maincontent']/div[@class='columns']/div[@class='column main']/div[@class='products wrapper grid products-grid']/ol[@class='products list items product-items']/li[1]/div[1]"
    echo_add_to_comp = "(//a[@title='Add to Compare'])[1]"
    gwen_hover = "//body/div[@class='page-wrapper']/main[@id='maincontent']/div[@class='columns']/div[@class='column main']/div[@class='products wrapper grid products-grid']/ol[@class='products list items product-items']/li[2]/div[1]"
    gwen_add_to_comp = "(//a[@title='Add to Compare'])[2]"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def wait_for_element(self, locator):
        # Method to wait for element before any action is committed
        self.logger.debug(f"Waiting for the element with locator: {locator}")
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, locator))
            )

    def click_echo_link(self):
        # Log the action and click on the designated link
        self.logger.debug(f"Clicking on the echo fit image")
        self.wait_for_element(self.echo_lnk).click()

    def add_echo_to_cart(self):
        # Log the action and click "add to cart" in the iframe
        self.logger.debug(f"Clicking on echo fit add to cart")
        self.wait_for_element(self.echo_add_to_cart).click()

    def add_echo_to_wishlist(self):
        # Log the action and click the heart icon in the iframe
        self.logger.debug(f"Clicking on echo fit  wishlist icon")
        self.wait_for_element(self.echo_add_to_wishlist).click()

    def click_echo_compare(self):
        # Log the action and click on "add to compare" icon
        self.logger.debug(f"Clicking on add to compare icon")
        act = ActionChains(self.driver)
        hover_element = self.wait_for_element(self.echo_hover)
        comp_element = self.wait_for_element(self.echo_add_to_comp)
        act.move_to_element(hover_element).move_to_element(comp_element).click().perform()

    def click_gwen_compare(self):
        # Log the action and click on "add to compare" icon
        self.logger.debug(f"Clicking on add to compare icon")
        act = ActionChains(self.driver)
        hover_element = self.wait_for_element(self.gwen_hover)
        comp_element = self.wait_for_element(self.gwen_add_to_comp)
        act.move_to_element(hover_element).move_to_element(comp_element).click().perform()

    def comparison_list_lnk(self):
        # Log the action and click on "comparison list" link
        self.logger.debug(f"Clicking on comparison list link")
        self.wait_for_element(self.comparison_lnk).click()

