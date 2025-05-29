# Import the necessary modules
from pageobjects.HomePage import HomePage
from pageobjects.YogaCollection import YogaCollection
from pageobjects.EchoFit import EchoFit
from pageobjects.ShoppingCart import ShoppingCart
from utilities.CustomLog import LogGenerator
from utilities.ReadProperties import ReadConfig
import pytest
import os

class TestAddToCart:
    # Get the URL, user email and password from the config file and initialize the logger
    baseURL = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGenerator.get_logger()

    @pytest.mark.sanity
    def test_add_to_cart(self, setup):
        # Log the action, define and create a path to save screenshots
        self.logger.info("*** Test_005_AddToCart started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            # Log the action and navigate to the main page
            self.logger.info("*** Navigate to the main page ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and click on the Yoga collection link
            self.logger.info("*** Click on the Yoga collection link ***")
            self.hp = HomePage(self.driver)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
            self.hp.click_luma_yoga_link()

            # Log the action and select Echo Fit Compression Short
            self.logger.info("*** Click on Echo Fit Compression Short")
            self.yc = YogaCollection(self.driver)
            self.yc.click_echo_link()

            # Log the action and select the required fields and add and navigate to cart
            self.logger.info("*** Adding to cart and navigating to cart page ***")
            self.ef = EchoFit(self.driver)
            self.ef.select_size_28()
            self.ef.select_colour_blue()
            self.ef.clear_quantity_field()
            self.ef.set_quantity(3)
            self.ef.add_to_cart()
            self.ef.click_shopping_cart_link()

            # Log the action and check that the item has been added to the cart
            self.logger.info("*** Navigate to Shopping Cart webpage and check for the item in the cart")
            self.sc = ShoppingCart(self.driver)
            self.head_title = self.sc.capt_head_title()
            self.sc_added_item = self.sc.capt_added_item()
            assert self.head_title == "Shopping Cart" and self.sc_added_item

            # Log the action and remove the items from the cart
            self.logger.info("*** Removing items from cart ***")
            self.sc.click_trash_icon()
            self.driver.quit()
            self.logger.info("*** Test_005_AddToCart Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_005_AddToCart Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_add_to_cart.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_005_AddToCart Complete ***")
