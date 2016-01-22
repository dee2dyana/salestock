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
    
    def test_order2(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        #sign in as an existing member
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("asd@abc.com")
        driver.find_element_by_id("passwd").clear()
        driver.find_element_by_id("passwd").send_keys("98765")
        driver.find_element_by_id("SubmitLogin").click()	
        #select item
        driver.find_element_by_xpath("//div[@id='block_top_menu']/ul/li[2]/a").click()
        driver.find_element_by_xpath("//div[@id='center_column']/ul/li[2]/div/div[2]/div[2]/a/span").click()
        driver.find_element_by_xpath("//div[@id='layer_cart']/div/div[2]/div[4]/a/span").click()
        #proceed to checkout
        driver.find_element_by_xpath("//div[@id='center_column']/p[2]/a/span").click()
        driver.find_element_by_name("processAddress").click()
        driver.find_element_by_id("cgv").click()
        driver.find_element_by_name("processCarrier").click()
        driver.find_element_by_link_text("Pay by check (order processing will be longer)").click()
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        driver.find_element_by_css_selector("p.alert.alert-success").click()
        try: self.assertEqual("Your order on My Store is complete.", driver.find_element_by_css_selector("p.alert.alert-success").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #sign out
        driver.find_element_by_link_text("Sign out").click()
        
    def tearDown(self):
        self.driver.close()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
