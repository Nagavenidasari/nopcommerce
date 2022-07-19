import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class AddCustomer:
    # Add all the customer page elaments

    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_submenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    btn_Addnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath="//*[@id='Email']"
    txtPassword_xpath="//*[@id='Password']"
    txtFname_xpath="//*[@id='FirstName']"
    txtLname_xpath="//*[@id='LastName']"
    rdMalegender_xpath="//*[@id='Gender_Male']"
    rdFemalegender_xpath="//*[@id='Gender_Female']"
    txtDoB_xpath="//*[@id='DateOfBirth']"
    txtCompanyname_xpath="//*[@id='Company']"
    txtCustomerroles_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemAdministrators_xpath="//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath="//li[contains(text(),'Registered')]"
    lstitemGuests_xpath="//li[contains(text(),'Guests')]"
    lstitemVendors_xpath="//li[contains(text(),'Vendors')]"
    lstitemForummoderators_xpath="//li[contains(text(),'Forum Moderators')]"
    drpManagerofvendor_xpath="//*[@id='VendorId']"
    txtAdmincomment_xpath="//*[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomer(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()
    def clickOnCustsubmenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_submenu_xpath).click()
    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btn_Addnew_xpath).click()
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)
    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH,self.rdMalegender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH,self.rdFemalegender_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.rdFemalegender_xpath).click()
    def setFname(self,fname):
        self.driver.find_element(By.XPATH,self.txtFname_xpath).send_keys(fname)
    def setLname(self,lname):
        self.driver.find_element(By.XPATH,self.txtLname_xpath).send_keys(lname)
    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.txtDoB_xpath).send_keys(dob)
    def setCompanyname(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyname_xpath).send_keys(comname)
    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerroles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
            self.driver.execute_script("arguments[0].click()", self.listitem)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
            self.driver.execute_script("arguments[0].click()", self.listitem)
        elif role == 'Guests':
            # User can only be a guest or registered but not both
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
            self.driver.execute_script("arguments[0].click()", self.listitem)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
            self.driver.execute_script("arguments[0].click()", self.listitem)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemForummoderators_xpath)
            self.driver.execute_script("arguments[0].click()", self.listitem)
        else:
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
            self.driver.execute_script("arguments[0].click()", self.listitem)


    def setManagerofVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drpManagerofvendor_xpath))
        #drp.select_by_visible_text(value)
        drp.select_by_index(value)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdmincomment_xpath).send_keys(content)
    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()





