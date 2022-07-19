import time
import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.Login import Login
from Utilities.readProperties import Readconfig
from Utilities.customLogging import LogGen
from Utilities import ExcelUtility

class Test_002_Login:
    #baseURL = "https://admin-demo.nop-commerce.com/"
    #baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    #username = "admin@yourstore.com"
    #password = "admin"
    baseURL = Readconfig.getApplicationURL()
    path = ".//Testdata/Login.xlsx"
    logger = LogGen.basiclogs()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.driver = setup
        setup.get(self.baseURL)
        self.lp = Login(setup)
        self.rows = ExcelUtility.getRowscount(self.path,'Sheet1')
        self.logger.info("******* Test_002 Login started **********")
        lst_status= [] #emptylist to update the status of the test
        for r in range(2,self.rows+1):
            self.username=ExcelUtility.readData(self.path,'Sheet1',r,1)
            self.password=ExcelUtility.readData(self.path,'Sheet1',r,2)
            self.exp=ExcelUtility.readData(self.path,'Sheet1',r,3)
            print(self.exp)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            time.sleep(3)
            #setup.implicitly_wait(self,8)
            self.lp.clickLogin()
            time.sleep(3)
            act_title = setup.title
            print(act_title)
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp =='Pass':
                    self.logger.info("**** Passed*******")
                    self.lp.clickLogout()
                    lst_status.append('Pass')
                    print(lst_status)
                elif self.exp == 'Fail':
                    self.logger.info("****Failed ****")
                    self.lp.clickLogout()
                    lst_status.append('Fail')
                    print(lst_status)
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("****Failed****")
                    lst_status.append('Fail')
                    print(lst_status)
                elif self.exp == 'Fail':
                    self.logger.info("*****Passed*****")
                    lst_status.append("Pass")
                    print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("********** DDT TESTCASE PASS****************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****DDT TEST Failed ******")
            self.driver.close()
            assert False
        self.logger.info("******* Test Completed*******")





