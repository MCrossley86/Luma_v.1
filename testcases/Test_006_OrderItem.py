# Import the necessary modules
from pageobjects.HomePage import HomePage
from pageobjects.CustomerLogin import CustLogin
from pageobjects.YogaCollection import YogaCollection
from pageobjects.EchoFit import EchoFit
from pageobjects.ShoppingCart import ShoppingCart
from pageobjects.OrderSummary import OrderSum
from pageobjects.OrderConfirmation import OrderConf
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
    def test_order_item(self, setup):
        # Log the action, define and create a path to save screenshots
        self.logger.info("*** Test_008_OrderItem started ***")
        self.driver = setup
        screenshots_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'screenshots')
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        try:
            # Log the action and navigate to the main page
            self.logger.info("*** Navigate to the main page ***")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            # Log the action and click the "Sign In" link
            self.logger.info("*** Click Sign In ***")
            self.hp = HomePage(self.driver)
            self.hp.click_sign_in_lnk()

            # Log the action and enter the required credentials into the corresponding fields
            self.logger.info("*** Sign into the application ***")
            self.cl = CustLogin(self.driver)
            self.cl.enter_email(self.user_email)
            self.cl.enter_pwd(self.password)
            self.cl.click_sign_in_btn()

            # Log the action and click on the Yoga collection link
            self.logger.info("*** Click on the Yoga collection link ***")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
            self.hp.click_luma_yoga_link()

            # Log the action and select Echo Fit Compression Short
            self.logger.info("*** Click on Echo Fit Compression Short ***")
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

            # Log the action and proceed to checkout
            self.logger.info("*** Navigate to Shopping Cart webpage and click checkout *** ")
            self.sc = ShoppingCart(self.driver)
            self.sc.click_checkout()

            # Log the action and proceed to order the item
            self.logger.info("*** Order the item *** ")
            self.os = OrderSum(self.driver)
            self.os.scroll_to_bottom()
            self.os.slct_ship_mthd()
            self.os.clck_nxt()
            self.os.scroll_to_bottom()
            self.os.clck_order()

            # Log the action and check that the item has been purchased
            self.logger.info("*** Checking that the item has been purchased")
            self.oc = OrderConf(self.driver)
            self.conf_head = self.oc.order_conf_head()
            assert self.conf_head == "Thank you for your purchase!"
            self.driver.quit()
            self.logger.info("*** Test_008_OrderItem Passed ***")

        except Exception as e:
            # Log the action and capture the screenshot of any failure
            self.logger.info("*** Test_008_OrderItem Failed ***")
            screenshot_filename = os.path.join(screenshots_path, "test_order_item.png")
            self.driver.save_screenshot(screenshot_filename)
            raise e
        self.logger.info("*** Test_008_OrderItem Complete ***")