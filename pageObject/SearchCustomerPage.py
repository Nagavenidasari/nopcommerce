import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SearchCustomer:
    txt_email_xpath ="//*[@id='SearchEmail']"
    grid_emailrow_xpath="//*[@id='customers-grid']/tbody/tr/td[2]"
    btn_search_xpath="//*[@id='search-customers']"

    def __init__(self, driver):
        self.driver = driver
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)
    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()
    def verifyEmail(self,email):
        searchedemail = self.driver.find_element(By.XPATH,self.grid_emailrow_xpath).text
        if searchedemail == email:
            return True
        else:
            return False

