from pageobjects.HomePage import MainPage
from pageobjects.CustomerLogin import CustLogin
from pageobjects.MyAccount import MyAccount
from utilities.CustomLog import LogGenerator
from utilities.ReadProperties import ReadConfig
from utilities import XLUtils
import pytest
import os
import time

class TestLogin_DDT:
    baseURL = ReadConfig.getapplicationurl()
    logger = LogGenerator.get_logger()
    #create path to XLutils
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "testdata", "LumaLoginDDT.xlsx")

    def test_login_ddt(self, setup):
        self.logger.info("*** Test_004_Login_DDT started ***")
        # Pull the required sheet from XLutils
        self.rows = XLUtils.getRowCount(self.path, 'loginDDT')
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.mp = MainPage(self.driver)
        self.cl = CustLogin(self.driver)
        self.ma = MyAccount(self.driver)

        # create a for loop to read all data in the excel sheet
        for r in range(2,self.rows+1):
            self.mp.clicksign()
        # setup XLUtils what data to capture
            self.email = XLUtils.readData(self.path, 'loginDDT',r,1)
            self.password = XLUtils.readData(self.path, 'loginDDT', r, 2)
            self.expected = XLUtils.readData(self.path, 'loginDDT', r, 3)
        # enter the details and check to see whether title is displayed
            self.cl.enteremail(self.email)
            self.cl.enterpwd(self.password)
            self.cl.clicksignin()
            self.target_page = self.cl.isMyAccountPageExists()
        # create the conditions on whether the login should be a pass or fail
            if self.expected=='Valid':
                if self.target_page==True:
                    lst_status.append('Pass')
                    self.ma.clickwelcome()
                    self.ma.clicksignout()
                else:
                    lst_status.append('Fail')
            elif self.expected=='Invalid':
                if self.target_page==True:
                    lst_status.append('Fail')
                    self.mp.clicksign()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        # the final validation
        if 'Fail' not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("*** Test_004_Login_DDT complete ***")

