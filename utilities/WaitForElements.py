# Import necessary modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.CustomLog import LogGenerator

def wait_for_element(driver, locator, timeout=10):
    # Log the action and wait for the element to be visible
    logger = LogGenerator.get_logger()
    logger.debug(f"Waiting for the element with locator: {locator}")
    return WebDriverWait(driver, timeout).until(ec.presence_of_element_located((By.XPATH, locator)))

def element_clickable(driver, locator, timeout=10):
    # Log the action and wait for the element to be clickable
    logger = LogGenerator.get_logger()
    logger.debug(f"Waiting for the element with locator: {locator}")
    return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable((By.XPATH, locator)))

def element_visible(driver, locator, timeout=10):
    # Log the action and wait for the element to be visible
    logger = LogGenerator.get_logger()
    logger.debug(f"Waiting for the element with locator: {locator}")
    return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.XPATH, locator)))

