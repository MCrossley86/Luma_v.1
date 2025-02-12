from pageobjects.HomePage import MainPage
from pageobjects.CustomerLogin import CustLogin
from pageobjects.MyAccount import MyAccount
from utilities.CustomLog import LogGenerator
from utilities.ReadProperties import ReadConfig
from utilities import XLUtils
import pytest
import os

class TestLoginDDT:
    baseURL = ReadConfig.getapplicationurl()
    logger = LogGenerator.get_logger()

    # Path to xl file
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "testdata", "LumaLoginDDT.xlsx")

    @pytest.mark.regression
    def test_login_ddt(self, setup):

        # Pull XLUtils file
        self.logger.info("*** Test_004_Login_DDT Started ***")
        self.rows = XLUtils.getRowCount(self.path, 'loginDDT')
        lst_status=[]

        self.logger.info("*** Open Browser ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.mp = MainPage(self.driver)
        self.cl = CustLogin(self.driver)
        self.ma = MyAccount(self.driver)

        # Create a for loop
        self.logger.info("*** Loop Start ***")
        for r in range(2,self.rows+1):
            self.mp.clicksign()

        # Read from XLUtils
            self.email = XLUtils.readData(self.path, 'loginDDT',r,1)
            self.password = XLUtils.readData(self.path, 'loginDDT', r, 2)
            self.expected = XLUtils.readData(self.path, 'loginDDT', r, 3)

        # Title check
            self.cl.enteremail(self.email)
            self.cl.enterpwd(self.password)
            self.cl.clicksignin()
            self.target_page = self.cl.ismyaccountpageexists()

        # Pass/Fail conditions
            if self.expected=='Valid':
                if self.target_page:
                    lst_status.append('Pass')
                    self.ma.clickwelcome()
                    self.ma.clicksignout()
                else:
                    lst_status.append('Fail')
            elif self.expected=='Invalid':
                if self.target_page:
                    lst_status.append('Fail')
                    self.cl.clear_email_field()
                    self.cl.clear_password_field()
                else:
                    lst_status.append('Pass')
        self.driver.close()

        # Final validation
        self.logger.info("*** lst_status check ***")
        if 'Fail' not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("*** Test_004_Login_DDT Complete ***")

