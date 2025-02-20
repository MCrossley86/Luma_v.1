# Import the necessary modules
from selenium.webdriver.common.by import By
from utilities.CustomLog import LogGenerator

class EchoFit:
    # Define locators for webpage elements
    echo_size_28 = "//div[contains(text(),'28')]"
    echo_colour_blue = "//div[contains(@option-label,'Blue')]"
    echo_quantity = "//input[@id='qty']"
    echo_add_to_cart_btn = "//button[@id='product-addtocart-button']"
    echo_cart_link = "//a[normalize-space()='shopping cart']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def select_size_28(self):
        # Log the action and click on size 28
        self.logger.debug(f"Clicking on size 28")
        self.driver.find_element(By.XPATH,self.echo_size_28).click()

    def select_colour_blue(self):
        # Log the action and click on the colour blue
        self.logger.debug(f"Clicking on blue")
        self.driver.find_element(By.XPATH,self.echo_colour_blue).click()

    def set_quantity(self, quantity):
        # Log the action and the quantity in the corresponding field
        self.logger.debug(f"Setting quantity: {quantity}")
        self.driver.find_element(By.XPATH,self.echo_quantity).send_keys(quantity)

    def add_to_cart(self):
        # Log the action and click on "add to cart" button
        self.logger.debug(f"Clicking on add to cart button")
        self.driver.find_element(By.XPATH,self.echo_add_to_cart_btn).click()

    def click_shopping_cart_link(self):
        # Log the action and click on "shopping cart" link
        self.logger.debug(f"Clicking on shopping cart link")
        self.driver.find_element(By.XPATH,self.echo_cart_link).click()
