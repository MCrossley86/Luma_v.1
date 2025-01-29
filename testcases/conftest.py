import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime
import os

# Launch Browser
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_addoption(parser):
    return parser.addoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser...")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser...")
    return driver

# HTML Reports
def pytest_configure(config):
    config.metadata = {}
    config.metadata['Project Name'] = "Luma_v.1"
    config.metadata['Module Name'] = "CustRegistration"
    config.metadata['QA'] = "Michael"

    html_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'reports')
    if not os.path.exists(html_path):
        os.makedirs(html_path)
    report_file = os.path.join(html_path, datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html")
    config.option.htmlpath = report_file

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



