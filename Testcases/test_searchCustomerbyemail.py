import pytest
import time
from pageObject.Login import Login
from pageObject.AddCustomerPage import AddCustomer
from pageObject.SearchCustomerPage import SearchCustomer
from Utilities.customLogging import LogGen
from Utilities.readProperties import Readconfig
from selenium.webdriver.common.by import By

class Test_004_SearchCustomer:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.basiclogs()

    @pytest.mark.regression
    def test_SearchCustomer(self,setup):
        self.logger.info("****** Test_004_SearchCustomer by Email******")
        self.driver = setup
        setup.get(self.baseURL)
        setup.maximize_window()
        self.lp = Login(setup)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful********")
        self.logger.info("******* Starting Search Customer*******")
        self.addcust = AddCustomer(setup)
        self.addcust.clickOnCustomer()
        self.addcust.clickOnCustsubmenu()
        self.logger.info("******* Searching Customer by Email *******")
        self.searchcust = SearchCustomer(setup)
        self.searchcust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchcust.clickSearch()
        time.sleep(5)
        status = self.searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        #assert True == status
        if status == True:
            self.logger.info("**************Test case Passed! *************")
        else:
            setup.save_screenshot(".\\Screenshots\\" + "t_searchcust.png")
            self.logger.error("************ Test case Failed ***************")
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
        setup.close()



