from selenium import webdriver
import pytest


class Test_Product():
    def test_Product_01(self,Setup):
        self.driver = Setup
        self.driver.find_element_by_id("user-name").send_keys("standard_user")
        self.driver.find_element_by_id("password").send_keys("secret_sauce")
        self.driver.find_element_by_id("login-button").click()
        
    
    def test_Product_02(self,Setup):
        self.driver = Setup
        self.driver.find_element_by_id("user-name").send_keys("standard_user")
        self.driver.find_element_by_id("password").send_keys("secret_sauce")
        self.driver.find_element_by_id("login-button").click()
