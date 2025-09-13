from selenium import webdriver
import pytest

class Test_Login():
    def test_login_01(self,Setup):
        self.driver = Setup
        self.driver.find_element_by_id("user-name").send_keys("standard_user")
        self.driver.find_element_by_id("password").send_keys("secret_sauce")
        self.driver.find_element_by_id("login-button").click()
        self.driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
        actual_num_of_Product= self.driver.find_element_by_xpath("//span[@class='shopping_cart_badge']").text
        expected_Element="2"
        assert actual_num_of_Product==expected_Element
    
    def test_login_02(self,Setup):
        self.driver = Setup
        self.driver.find_element_by_id("user-name").send_keys("standard_user")
        self.driver.find_element_by_id("password").send_keys("secret_sauce")
        self.driver.find_element_by_id("login-button").click()
        self.driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
        actual_num_of_Product= self.driver.find_element_by_xpath("//span[@class='shopping_cart_badge']").text
        expected_Element="2"
        assert actual_num_of_Product==expected_Element


    
        
    
        

