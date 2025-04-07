# Import the necessary modules
from pageobjects.HomePage import MainPage
from pageobjects.CustomerLogin import CustLogin
from pageobjects.MyAccount import MyAccount
from utilities.CustomLog import LogGenerator
from utilities.ReadProperties import ReadConfig
from utilities import XLUtils
import pytest
import os

class TestLoginDDT:
    # Get the URL from the config file, initialize the logger and create a path to the Excel file containing the data
    baseURL = ReadConfig.get_application_url()
    logger = LogGenerator.get_logger()
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "testdata", "LumaLoginDDT.xlsx")

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        # Log the action, get the number of rows in the Excel sheet and create a blank list
        self.logger.info("*** Test_004_Login_DDT Started ***")
        self.rows = XLUtils.get_row_count(self.path, 'loginDDT')
        lst_status=[]

        # Log the action and navigate to the main page
        self.logger.info("*** Navigate to the main page ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Initialize page objects
        self.mp = MainPage(self.driver)
        self.cl = CustLogin(self.driver)
        self.ma = MyAccount(self.driver)

        # Log the action and iterate through the rows in the Excel sheet
        self.logger.info("*** Loop Start ***")
        for r in range(2,self.rows+1):
            self.mp.click_sign()

            # Log the action and read email, password, and expected result from the Excel sheet
            self.logger.info("*** Read data from the Excel sheet ***")
            self.email = XLUtils.read_data(self.path, 'loginDDT',r,1)
            self.password = XLUtils.read_data(self.path, 'loginDDT', r, 2)
            self.expected = XLUtils.read_data(self.path, 'loginDDT', r, 3)

            # Log the action, enter credentials, click the sign-in button then check if the header is displayed
            self.logger.info("*** Sign into the application ***")
            self.cl.enter_email(self.email)
            self.cl.enter_pwd(self.password)
            self.cl.click_signin()
            self.target_page = self.cl.is_my_account_page_exists()

            # Log the action and determine pass/fail status based on the expected result
            self.logger.info("*** Log login results ***")
            if self.expected=='Valid':
                if self.target_page:
                    lst_status.append('Pass')
                    self.ma.click_welcome()
                    self.ma.click_sign_out()
                else:
                    lst_status.append('Fail')
            elif self.expected=='Invalid':
                if self.target_page:
                    lst_status.append('Fail')
                    self.cl.clear_email_field()
                    self.cl.clear_password_field()
                else:
                    lst_status.append('Pass')
        self.driver.quit()

        # Log the action and assert the final result based on the status of the list
        self.logger.info("*** lst_status check ***")
        if 'Fail' not in lst_status:
            self.logger.info("*** Test_004_Login_DDT Pass ***")
            assert True
        else:
            self.logger.info("*** Test_004_Login_DDT Fail ***")
            assert False
        self.logger.info("*** Test_004_Login_DDT Complete ***")

