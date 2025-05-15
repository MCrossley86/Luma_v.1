# Import the necessary modules
from utilities.WaitForElements import wait_for_element
from utilities.WaitForElements import element_clickable
from selenium.webdriver import ActionChains
from utilities.CustomLog import LogGenerator

class NavBarHP:
    # Define locators for webpage elements
    whats_new_lnk = "(//a[@id='ui-id-3'])[1]"
    w_lnk = "(//a[@id='ui-id-4'])[1]"
    w_tops_lnk = "(//a[@id='ui-id-9'])[1]"
    w_jacket_lnk = "(//a[@id='ui-id-11'])[1]"
    w_hoodies_sweatshirts_lnk = "(//a[@id='ui-id-12'])[1]"
    w_tees_lnk = "(//a[@id='ui-id-13'])[1]"
    w_bras_tanks_lnk = "(//a[@id='ui-id-14'])[1]"
    w_bottoms_lnk = "(//a[@id='ui-id-10'])[1]"
    w_pants_lnk = "(//a[@id='ui-id-15'])[1]"
    w_shorts_lnk = "(//a[@id='ui-id-16'])[1]"
    m_lnk = "(//a[@id='ui-id-5'])[1]"
    head_conf = "//span[@class='base']"

    def __init__(self, driver):
        # Initialize the driver and logger
        self.driver = driver
        self.logger = LogGenerator.get_logger()

    def click_whats_new_lnk(self):
        # Log the action and click the "What's New" link
        self.logger.debug(f"Clicking the What's New link")
        wait_for_element(self.driver, self.whats_new_lnk).click()

    def click_women_lnk(self):
        # Log the action and click the "Women" link
        self.logger.debug(f"Clicking the Women link")
        wait_for_element(self.driver, self.w_lnk).click()

    def click_w_tops_lnk(self):
        # Log the action and click on "tops" link in the women tab in the nav bar
        self.logger.debug(f"Clicking on the tops link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.w_lnk)
        comp_element = wait_for_element(self.driver, self.w_tops_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(comp_element).click().perform()

    def click_w_jackets_lnk(self):
        # Log the action and click on "jackets" link in the women tab in the nav bar
        self.logger.debug(f"Clicking on the jackets link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.w_lnk)
        hover_element_3 = wait_for_element(self.driver, self.w_tops_lnk)
        comp_element = wait_for_element(self.driver, self.w_jacket_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_w_hoodies_sweatshirts_lnk(self):
        # Log the action and click on "hoodies and sweatshirts" link in the women tab in the nav bar
        self.logger.debug(f"Clicking on the hoodies and sweatshirts link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.w_lnk)
        hover_element_3 = wait_for_element(self.driver, self.w_tops_lnk)
        comp_element = wait_for_element(self.driver, self.w_hoodies_sweatshirts_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_w_tees_lnk(self):
        # Log the action and click on "tees" link in the women tab in the nav bar
        self.logger.debug(f"Clicking on the tees link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.w_lnk)
        hover_element_3 = wait_for_element(self.driver, self.w_tops_lnk)
        comp_element = wait_for_element(self.driver, self.w_tees_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_w_bras_tanks_lnk(self):
        # Log the action and click on "bras and tanks" link in the women tab in the nav bar
        self.logger.debug(f"Clicking on the bras and tanks link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.w_lnk)
        hover_element_3 = wait_for_element(self.driver, self.w_tops_lnk)
        comp_element = wait_for_element(self.driver, self.w_bras_tanks_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_w_bottoms_lnk(self):
        # Log the action and click on "bottoms" link in the women tab in the nav bar
        self.logger.debug(f"Clicking on the bottoms link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.w_lnk)
        comp_element = wait_for_element(self.driver, self.w_bottoms_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(comp_element).click().perform()

    def click_w_pants_lnk(self):
        # Log the action and click on "pants" link in the women tab in the nav bar
        self.logger.debug(f"Clicking on the pants link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.w_lnk)
        hover_element_3 = wait_for_element(self.driver, self.w_bottoms_lnk)
        comp_element = wait_for_element(self.driver, self.w_pants_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_w_shorts_lnk(self):
        # Log the action and click on "shorts" link in the women tab in the nav bar
        self.logger.debug(f"Clicking on the shorts link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.w_lnk)
        hover_element_3 = wait_for_element(self.driver, self.w_bottoms_lnk)
        comp_element = wait_for_element(self.driver, self.w_shorts_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def capt_header_title(self):
        # Capture the header title text and handle any exceptions
        try:
            return wait_for_element(self.driver, self.head_conf).text
        except Exception as e:
            self.logger.error(f"Error retrieving head title: {e}")
            return None

