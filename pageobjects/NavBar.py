# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from selenium.webdriver import ActionChains
from utilities.CustomLog import LogGenerator

class NavBarHP:
    # Define locators for webpage elements
    whats_new_link = "//a[@id='ui-id-3']//span[1]"
    women_link = "//a[@id='ui-id-4']//span[1]"
    w_tops_lnk = "(//span[contains(text(),'Tops')])[1]"
    w_nav_hover = "//a[@id='ui-id-4']//span[1]"
    w_tops_click = "(//span[contains(text(),'Tops')])[1]"
    men_link = "//a[@id='ui-id-5']//span[1]"
    gear_link = "//a[@id='ui-id-6']//span[1]"
    training_link = "//a[@id='ui-id-7']//span[1]"
    sale_link = "//a[@id='ui-id-8']//span[1]"
    title_header = "//span[@class='base']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def click_whats_new(self):
        # Log the action and click on "What's New" in the nav bar
        self.logger.debug(f"Clicking on What's New")
        wait_for_element(self.driver, self.whats_new_link).click()

    def click_women(self):
        # Log the action and click on "Women" in the nav bar
        self.logger.debug(f"Clicking on Women")
        wait_for_element(self.driver, self.women_link).click()

    def click_men(self):
        # Log the action and click on "Men" in the nav bar
        self.logger.debug(f"Clicking on Men")
        wait_for_element(self.driver, self.men_link).click()

    def click_gear(self):
        # Log the action and click on "Gear" in the nav bar
        self.logger.debug(f"Clicking on Gear")
        wait_for_element(self.driver, self.gear_link).click()

    def click_training(self):
        # Log the action and click on "Training" in the nav bar
        self.logger.debug(f"Clicking on Training")
        wait_for_element(self.driver, self.training_link).click()

    def click_sale(self):
        # Log the action and click on "Sale" in the nav bar
        self.logger.debug(f"Clicking on Sale")
        wait_for_element(self.driver, self.sale_link).click()

    def whats_new_title(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = wait_for_element(self.driver, self.title_header).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def women_title(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = wait_for_element(self.driver, self.title_header).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def women_tops_click(self):
        # Log the action and click on "Tops" in the nav bar women section
        self.logger.debug(f"Clicking on Tops in the women section")
        act = ActionChains(self.driver)
        hover_element = wait_for_element(self.driver, self.w_nav_hover)
        comp_element = wait_for_element(self.driver, self.w_tops_click)
        act.move_to_element(hover_element).move_to_element(comp_element).click().perform()

    def w_tops_title(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = wait_for_element(self.driver, self.title_header).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def men_title(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = wait_for_element(self.driver, self.title_header).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def gear_title(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = wait_for_element(self.driver, self.title_header).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def training_title(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = wait_for_element(self.driver, self.title_header).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def sale_title(self):
        # Log the action and capture the header text
        self.logger.debug(f"Capturing header text")
        try:
            text_capture = wait_for_element(self.driver, self.title_header).text
            print("Text captured")
            return text_capture
        except Exception as e:
            print(f"An error occurred: {e}")
            return False