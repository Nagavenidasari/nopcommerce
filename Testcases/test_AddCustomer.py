
import pytest
import time
from pageObject.Login import Login
from pageObject.AddCustomerPage import AddCustomer
from Utilities.customLogging import LogGen
from Utilities.readProperties import Readconfig
from selenium.webdriver.common.by import By
import string
import random

class Test_003_AddCustomer:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.basiclogs()

    @pytest.mark.sanity
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
        self.logger.info("********* Adding Customer Details *******")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        time.sleep(3)
        self.addcust.setPassword("test123")
        self.addcust.setFname("Nagaraj")
        self.addcust.setLname("Kathaiwadi")
        self.addcust.setGender("Male")
        self.addcust.setDob("7/05/1988")
        self.addcust.setCompanyname("Sai Labs")
        #self.addcust.setCustomerRoles("Registered")
        #self.addcust.drpManagerofvendor_xpath(3)
        self.addcust.setAdminContent("This is for testing .....")
        self.addcust.clickOnSave()
        self.logger.info("****** Saving Customer Info ********")
        self.logger.info("********* Add customer Validation started ********")
        #self.msg = self.driver.find_element(By.TAG_NAME,"body").text()
        #self.msg = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/form/div[2]").text()
        #self.msg = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div").text()
        #self.msg=self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]").text
        self.msg=self.driver.find_element(By.CSS_SELECTOR,"body > div.wrapper > div.content-wrapper > div.alert.alert-success.alert-dismissable").text

        print(self.msg)
        if 'The new customer has been added successfully.' not in self.msg:
            setup.save_screenshot(".\\Screenshots\\"+"t_addcust.png")
            self.logger.error("******** Add Customer Testcase Failed ********")
            assert False

        else:
            assert True
            self.logger.info("***** Add Customer Testcase Passed *******")

        self.driver.close()
        self.logger.info("*********Ending Add Customer Test ********")



    # This method generates and returns a radom email
def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))