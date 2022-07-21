import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SearchCustomer:
    txt_email_xpath ="//*[@id='SearchEmail']"
    grid_emailrow_xpath="//*[@id='customers-grid']/tbody/tr/td[2]"
    btn_search_xpath="//*[@id='search-customers']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)
    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()
    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element(By.XPATH,self.table_xpath)
          emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag

