import pytest
import time
from pageObject.Login import Login
from Utilities.customLogging import LogGen
from Utilities.readProperties import Readconfig
from selenium.webdriver.common.by import By
from pageObject.Checkorders import Checkorders

class Test_005_Orderstatus:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.basiclogs()

    @pytest.mark.regression
    def test_OrderStatus(self,setup):
        self.logger.info("****** Test_005_Searchorderstatus******")
        self.driver = setup
        setup.get(self.baseURL)
        setup.maximize_window()
        self.lp = Login(setup)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful********")
        self.logger.info("******* Starting Search Orderstatus *******")
        time.sleep(4)
        self.logger.info("********* Clicking on Sales*********")
        self.orderstatus = Checkorders(setup)
        self.orderstatus.clickonSales()
        self.orderstatus.clickonOrders()
        time.sleep(4)
        self.orderstatus.clickonCollapse()
        self.logger.info("********** Checking the Pending Status*************")
        count = self.orderstatus.searchOrderStatus("Pending")
        if count != 0:
            self.logger.info("**************Test case Passed! *************")
        else:
            setup.save_screenshot(".\\Screenshots\\" + "t_orderstatus.png")
            self.logger.error("************ Test case Failed ***************")
        self.logger.info("***************  TC_Orderstatus 005 is Finished  *********** ")
        setup.close()
