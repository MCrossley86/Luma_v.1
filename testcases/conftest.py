# Import the necessary modules
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime
import os

@pytest.fixture()
# Fixture to get the browser option from the command line arguments
def browser(request):
    return request.config.getoption("--browser")

# Add the browser option to the command line arguments
def pytest_addoption(parser):
    return parser.addoption("--browser")

@pytest.fixture()
# Fixture to set up the browser driver based on the selected browser option
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

# Configure HTML reports for the test results
def pytest_configure(config):
    config.metadata = {'Project Name': "Luma_v.1", 'Module Name': "CustRegistration", 'QA': "Michael"}

    # Create the directory for the HTML report if it doesn't exist
    html_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'reports')
    if not os.path.exists(html_path):
        os.makedirs(html_path)

    # Generate the HTML report file name with the current date and time
    report_file = os.path.join(html_path, datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html")
    config.option.htmlpath = report_file

@pytest.hookimpl(optionalhook=True)
# Remove specific metadata from the HTML report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)