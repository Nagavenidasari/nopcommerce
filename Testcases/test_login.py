import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.Login import Login
from Utilities.readProperties import Readconfig
from Utilities.customLogging import LogGen


class Test_001_Login:
    #baseURL = "https://admin-demo.nop-commerce.com/"
    #baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    #username = "admin@yourstore.com"
    #password = "admin"
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.basiclogs()



    @pytest.mark.regression
    def test_homePage(self,setup):

        print("testing home page with logging")
        self.logger.info("***********Test_001_Login**************")
        self.logger.info("*************** Verifying Homepage Title **********")
        print("printed two log statements")
        self.driver = setup
        setup.get(self.baseURL)
        act_title = setup.title
        print(act_title)

        if act_title == "Your Store. Login":
            assert True
            setup.close()
            self.logger.info("*******test_homepage Passed !******")
        else:
            time.sleep(3)
            setup.save_screenshot(".\\Screenshots\\"+"t_homepageTitle.png")
            #time.sleep(3)
            #setup.save_screenshot('//Screenshots/testHome_Page.png')
            setup.close()
            self.logger.error("%%%%%%%%%%%% Test_homepage Failed .....  %%%%%%%%")
            assert False

    @pytest.mark.sanity
    def test_login(self,setup):
        self.driver = setup
        setup.get(self.baseURL)
        self.lp = Login(setup)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = setup.title
        print(act_title)

        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("************ Login Test case Passed *********")
            setup.close()
            assert True
        else:
            self.logger.error("%%%%%% Login Test Failed.... %%%%%%%%")
            setup.close()
            assert False


