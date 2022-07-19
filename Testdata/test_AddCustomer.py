import pytest
import time
from pageObject.Login import Login
from pageObject.AddCustomerPage import AddCustomer
from Utilities.customLogging import LogGen
from Utilities.readProperties import Readconfig
import string
import random

class Test_003_AddCustomer:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.basiclogs()

    # This method generates and returns a radom email
    def random_generaor(size=8,chars=string.ascii_lowercase+string.digits):
        return ''.join(random.choice(chars) for x in range(size))
    def test_addCustomer(self,setup):
        self.logger.info("****** Test_003_AddCustomer******")
        self.driver = setup
        setup.get(self.baseURL)
        setup.maximize_window()
        self.lp = Login(setup)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful********")
        self.logger.info("******* Starting Add Customer*******")
        self.addcust = AddCustomer(setup)
        self.addcust.clickOnCustomer()
        self.addcust.clickOnCustsubmenu()
        self.addcust.clickOnAddnew()
        self.logger("********* Adding Customer Details *******")
        setup.close()