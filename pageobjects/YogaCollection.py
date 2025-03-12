# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from selenium.webdriver import ActionChains
from utilities.CustomLog import LogGenerator

class YogaCollection:
    # Define locators for webpage elements
    echo_lnk = "//a[@class='product photo product-item-photo']//img[@alt='Echo Fit Compression Short']"
    comparison_lnk = "//a[normalize-space()='comparison list']"
    echo_add_to_cart = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/button[1]/span[1]"
    echo_hover = "//body/div[@class='page-wrapper']/main[@id='maincontent']/div[@class='columns']/div[@class='column main']/div[@class='products wrapper grid products-grid']/ol[@class='products list items product-items']/li[1]/div[1]"
    echo_add_to_comp = "(//a[@title='Add to Compare'])[1]"
    gwen_hover = "//body/div[@class='page-wrapper']/main[@id='maincontent']/div[@class='columns']/div[@class='column main']/div[@class='products wrapper grid products-grid']/ol[@class='products list items product-items']/li[2]/div[1]"
    gwen_add_to_comp = "(//a[@title='Add to Compare'])[2]"
    fiona_hover = "//body/div[@class='page-wrapper']/main[@id='maincontent']/div[@class='columns']/div[@class='column main']/div[@class='products wrapper grid products-grid']/ol[@class='products list items product-items']/li[3]/div[1]"
    fiona_add_to_wishlist = "(//a[@title='Add to Wish List'])[3]"


    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def click_echo_link(self):
        # Log the action and click on the designated link
        self.logger.debug(f"Clicking on the echo fit image")
        wait_for_element(self.driver, self.echo_lnk).click()

    def add_echo_to_cart(self):
        # Log the action and click "add to cart" in the iframe
        self.logger.debug(f"Clicking on echo fit add to cart")
        wait_for_element(self.driver, self.echo_add_to_cart).click()

    def click_echo_compare(self):
        # Log the action and click on "add to compare" icon
        self.logger.debug(f"Clicking on add to compare icon")
        act = ActionChains(self.driver)
        hover_element = wait_for_element(self.driver, self.echo_hover)
        comp_element = wait_for_element(self.driver, self.echo_add_to_comp)
        act.move_to_element(hover_element).move_to_element(comp_element).click().perform()

    def click_gwen_compare(self):
        # Log the action and click on "add to compare" icon
        self.logger.debug(f"Clicking on add to compare icon")
        act = ActionChains(self.driver)
        hover_element = wait_for_element(self.driver, self.gwen_hover)
        comp_element = wait_for_element(self.driver, self.gwen_add_to_comp)
        act.move_to_element(hover_element).move_to_element(comp_element).click().perform()

    def click_fiona_wishlist(self):
        # Log the action and click on "add to wishlist" icon
        self.logger.debug(f"Clicking on add to wishlist icon")
        act = ActionChains(self.driver)
        hover_element = wait_for_element(self.driver, self.fiona_hover)
        comp_element = wait_for_element(self.driver, self.fiona_add_to_wishlist)
        act.move_to_element(hover_element).move_to_element(comp_element).click().perform()

    def comparison_list_lnk(self):
        # Log the action and click on "comparison list" link
        self.logger.debug(f"Clicking on comparison list link")
        wait_for_element(self.driver, self.comparison_lnk).click()

