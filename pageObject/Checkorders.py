import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Checkorders:
    linkSalesmenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/a"
    linkclickorders_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[1]/a"
    btncollapse_xpath = "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[1]/div[3]"
    table_xpath = "//*[@id='orders-grid']"
    tblerows_xpath = "//*[@id='orders-grid']/tbody/tr"
    tblcols_xpath = "//*[@id='orders-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def clickonSales(self):
        self.driver.find_element(By.XPATH, self.linkSalesmenu_xpath).click()

    def clickonOrders(self):
        self.driver.find_element(By.XPATH, self.linkclickorders_xpath).click()

    def clickonCollapse(self):
        self.driver.find_element(By.XPATH, self.btncollapse_xpath).click()

    def getRowlenghth(self):
        return len(self.driver.find_elements(By.XPATH, self.tblerows_xpath))

    def getCollength(self):
        return len(self.driver.find_elements(By.XPATH, self.tblcols_xpath))

    def searchOrderStatus(self, status):
        count=0
        orderstatus = []
        for r in range(1, self.getRowlenghth() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            stat = table.find_element(By.XPATH, "//table[@id='orders-grid']/tbody/tr["+str(r)+"]/td[4]").text
            orderstatus.append(stat)
        for p in range(len(orderstatus)):
            if orderstatus[p] == status:
                print("Found at index", status, p)
                count = count+1
                print("Count is ",count)

            #   print(ordstatus)
            #  flag = True
            # break
        return count
