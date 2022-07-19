from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time
from selenium.webdriver.support import wait

class Login:
    # Define all the locators
    #textbox_username_id = "Email"
    textbox_username_xpath = "//*[@id='Email']"
    textbox_password_xp = "//*[@id='Password']"
    button_login_xpath ="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        time.sleep(3)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        time.sleep(2)
        #self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        #self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xp).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.textbox_password_xp).send_keys(password)
    def clickLogin(self):
        self.driver.implicitly_wait(8)
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()
