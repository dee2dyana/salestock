# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest

class Salestock(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_salestock(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        #search empty field
        driver.find_element_by_id("search_query_top").click()
        driver.find_element_by_name("submit_search").click()
		    #not found
        self.assertEqual("0 results have been found.", driver.find_element_by_css_selector("span.heading-counter").text)
        driver.find_element_by_id("search_query_top").clear()
        #search "dress"
        driver.find_element_by_id("search_query_top").send_keys("dress")
        driver.find_element_by_name("submit_search").click() #dresses are listed
	      #sort by price: lowest first
        Select(driver.find_element_by_id("selectProductSort")).select_by_visible_text("Price: Lowest first")
        driver.find_element_by_link_text("List").click()
        driver.find_element_by_link_text("Grid").click()
        Select(driver.find_element_by_id("selectProductSort")).select_by_visible_text("Price: Highest first")
        Select(driver.find_element_by_id("selectProductSort")).select_by_visible_text("Product Name: A to Z")
        Select(driver.find_element_by_id("selectProductSort")).select_by_visible_text("Product Name: Z to A")
        Select(driver.find_element_by_id("selectProductSort")).select_by_visible_text("In stock")
        Select(driver.find_element_by_id("selectProductSort")).select_by_visible_text("Reference: Lowest first")
        Select(driver.find_element_by_id("selectProductSort")).select_by_visible_text("Reference: Highest first")
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
