# Import necessary modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.CustomLog import LogGenerator

def wait_for_element(driver, locator, timeout=10):
    logger = LogGenerator.get_logger()
    logger.debug(f"Waiting for the element with locator: {locator}")
    return WebDriverWait(driver, timeout).until(ec.presence_of_element_located((By.XPATH, locator)))