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
    m_tops_lnk = "(//a[@id='ui-id-17'])[1]"
    m_jacket_lnk = "(//a[@id='ui-id-19'])[1]"
    m_hoodies_sweatshirts_lnk = "(//a[@id='ui-id-20'])[1]"
    m_tees_lnk = "(//a[@id='ui-id-21'])[1]"
    m_tanks_lnk = "(//a[@id='ui-id-22'])[1]"
    m_bottoms_lnk = "(//a[@id='ui-id-18'])[1]"
    m_pants_lnk = "(//a[@id='ui-id-23'])[1]"
    m_shorts_lnk = "(//a[@id='ui-id-24'])[1]"
    g_lnk = "(//a[@id='ui-id-6'])[1]"
    bags_lnk = "(//a[@id='ui-id-25'])[1]"
    fit_equip_lnk = "(//a[@id='ui-id-26'])[1]"
    watch_lnk = "(//a[@id='ui-id-27'])[1]"
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

    def click_men_lnk(self):
        # Log the action and click the "Men" link
        self.logger.debug(f"Clicking the Men link")
        wait_for_element(self.driver, self.m_lnk).click()

    def click_m_tops_lnk(self):
        # Log the action and click on "tops" link in the men tab in the nav bar
        self.logger.debug(f"Clicking on the tops link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.w_lnk)
        hover_element_2 = wait_for_element(self.driver, self.m_lnk)
        comp_element = wait_for_element(self.driver, self.m_tops_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(comp_element).click().perform()

    def click_m_jackets_lnk(self):
        # Log the action and click on "jackets" link in the men tab in the nav bar
        self.logger.debug(f"Clicking on the jackets link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.w_lnk)
        hover_element_2 = wait_for_element(self.driver, self.m_lnk)
        hover_element_3 = wait_for_element(self.driver, self.m_tops_lnk)
        comp_element = wait_for_element(self.driver, self.m_jacket_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_m_hoodies_sweatshirts_lnk(self):
        # Log the action and click on "hoodies and sweatshirts" link in the men tab in the nav bar
        self.logger.debug(f"Clicking on the hoodies and sweatshirts link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.w_lnk)
        hover_element_2 = wait_for_element(self.driver, self.m_lnk)
        hover_element_3 = wait_for_element(self.driver, self.m_tops_lnk)
        comp_element = wait_for_element(self.driver, self.m_hoodies_sweatshirts_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_m_tees_lnk(self):
        # Log the action and click on "tees" link in the men tab in the nav bar
        self.logger.debug(f"Clicking on the tees link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.w_lnk)
        hover_element_2 = wait_for_element(self.driver, self.m_lnk)
        hover_element_3 = wait_for_element(self.driver, self.m_tops_lnk)
        comp_element = wait_for_element(self.driver, self.m_tees_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_m_tanks_lnk(self):
        # Log the action and click on "tanks" link in the men tab in the nav bar
        self.logger.debug(f"Clicking on the tanks link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.w_lnk)
        hover_element_2 = wait_for_element(self.driver, self.m_lnk)
        hover_element_3 = wait_for_element(self.driver, self.m_tops_lnk)
        comp_element = wait_for_element(self.driver, self.m_tanks_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_m_bottoms_lnk(self):
        # Log the action and click on "bottoms" link in the men tab in the nav bar
        self.logger.debug(f"Clicking on the bottoms link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.w_lnk)
        hover_element_2 = wait_for_element(self.driver, self.m_lnk)
        comp_element = wait_for_element(self.driver, self.m_bottoms_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(comp_element).click().perform()

    def click_m_pants_lnk(self):
        # Log the action and click on "pants" link in the men tab in the nav bar
        self.logger.debug(f"Clicking on the pants link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.w_lnk)
        hover_element_2 = wait_for_element(self.driver, self.m_lnk)
        hover_element_3 = wait_for_element(self.driver, self.m_bottoms_lnk)
        comp_element = wait_for_element(self.driver, self.m_pants_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_m_shorts_lnk(self):
        # Log the action and click on "shorts" link in the men tab in the nav bar
        self.logger.debug(f"Clicking on the shorts link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.w_lnk)
        hover_element_2 = wait_for_element(self.driver, self.m_lnk)
        hover_element_3 = wait_for_element(self.driver, self.m_bottoms_lnk)
        comp_element = wait_for_element(self.driver, self.m_shorts_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(hover_element_3).move_to_element(comp_element).click().perform()

    def click_gear_lnk(self):
        # Log the action and click the "Gear" link
        self.logger.debug(f"Clicking the Gear link")
        wait_for_element(self.driver, self.g_lnk).click()

    def click_bag_lnk(self):
        # Log the action and click on "bag" link in the gears tab in the nav bar
        self.logger.debug(f"Clicking on the bottoms link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.g_lnk)
        comp_element = wait_for_element(self.driver, self.bags_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(comp_element).click().perform()

    def click_fit_equip_lnk(self):
        # Log the action and click on "fitness and equipment" link in the gears tab in the nav bar
        self.logger.debug(f"Clicking on the bottoms link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.g_lnk)
        comp_element = wait_for_element(self.driver, self.fit_equip_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(comp_element).click().perform()

    def click_watches_lnk(self):
        # Log the action and click on "watches" link in the gears tab in the nav bar
        self.logger.debug(f"Clicking on the bottoms link")
        act = ActionChains(self.driver)
        hover_element_1 = wait_for_element(self.driver, self.m_lnk)
        hover_element_2 = wait_for_element(self.driver, self.g_lnk)
        comp_element = wait_for_element(self.driver, self.watch_lnk)
        act.move_to_element(hover_element_1).move_to_element(hover_element_2).move_to_element(comp_element).click().perform()

    def capt_header_title(self):
        # Capture the header title text and handle any exceptions
        try:
            return wait_for_element(self.driver, self.head_conf).text
        except Exception as e:
            self.logger.error(f"Error retrieving head title: {e}")
            return None

