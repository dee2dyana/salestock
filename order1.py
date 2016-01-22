# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest

class Order1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_order1(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        #select item, add to cart
        driver.find_element_by_css_selector("div.columns-container").click()
        driver.find_element_by_xpath("//ul[@id='homefeatured']/li/div/div[2]/div[2]/a/span").click()
        driver.find_element_by_xpath("//div[@id='layer_cart']/div/div[2]/div[4]/a/span").click()
        driver.find_element_by_xpath("//div[@id='center_column']/p[2]/a/span").click()
        driver.find_element_by_id("center_column").click()
        #register new member
        driver.find_element_by_id("email_create").send_keys("test1@abc.com")
        driver.find_element_by_id("SubmitCreate").click()
		    #filled in personal information
        driver.find_element_by_id("id_gender2").click()
        driver.find_element_by_id("customer_firstname").clear()
        driver.find_element_by_id("customer_firstname").send_keys("asd")
        driver.find_element_by_id("customer_lastname").clear()
        driver.find_element_by_id("customer_lastname").send_keys("abc")
        driver.find_element_by_id("passwd").clear()
        driver.find_element_by_id("passwd").send_keys("98765")
        driver.find_element_by_id("address1").clear()
        driver.find_element_by_id("address1").send_keys("jl kota 23223")
        driver.find_element_by_id("city").clear()
        driver.find_element_by_id("city").send_keys("jakarta")
        Select(driver.find_element_by_id("id_state")).select_by_visible_text("Alaska")
        driver.find_element_by_css_selector("#id_state > option[value=\"2\"]").click()
        driver.find_element_by_id("postcode").click()
        driver.find_element_by_id("postcode").clear()
        driver.find_element_by_id("postcode").send_keys("23223")
        driver.find_element_by_id("phone_mobile").clear()
        driver.find_element_by_id("phone_mobile").send_keys("0987654321")
        driver.find_element_by_id("alias").clear()
        driver.find_element_by_id("alias").send_keys("My addressasd")
        driver.find_element_by_id("alias").clear()
        driver.find_element_by_id("alias").send_keys("12ss")
        driver.find_element_by_id("submitAccount").click()
        #proceed to checkout
        driver.find_element_by_name("processAddress").click()
        driver.find_element_by_id("cgv").click()
        driver.find_element_by_name("processCarrier").click()
        driver.find_element_by_link_text("Pay by check (order processing will be longer)").click()
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        
    
    def tearDown(self):
        self.driver.close()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
