# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as FirefoxService

class TestTestCase5():
  def setup_method(self, method):
    browser_name = "edge"
    if browser_name == "chrome":
      chrome_driver_binary = r'.\drivers\chromedriver'
      self.driver = webdriver.Chrome(chrome_driver_binary)
      self.vars = {}
    elif browser_name == "firefox":
      firefox_driver_binary = r'.\drivers\geckodriver'
      ser_firefox = FirefoxService(firefox_driver_binary)
      self.driver = webdriver.Firefox(service=ser_firefox)
    else:
      edge_driver_binary = r'.\drivers\msedgedriver'
      self.driver = webdriver.Edge(edge_driver_binary)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testCase5_first_search(self):
    self.driver.get("https://www.ebay.com/")
    self.driver.set_window_size(1552, 840)
    element = self.driver.find_element(By.CSS_SELECTOR, "#mainContent > div.hl-cat-nav > ul > li:nth-child(3) > a")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "Apple").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".b-visualnav__tile:nth-child(1) .b-img").click()
    time.sleep(5)
    element = self.driver.find_element(By.CSS_SELECTOR, ".carousel__snap-point:nth-child(1) .b-img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel__snap-point:nth-child(1) .b-img").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".x-item-title__mainTitle").click()
    time.sleep(5)
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .seo-breadcrumb-text > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "gh-ac").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR,"#gh-la").click()
    time.sleep(5)
    self.driver.find_element(By.ID, "gh-ac").send_keys("Apple iPhone 11 64GB Factory Unlocked AT&T T-Mobile Verizon Very Good Condition")
    self.driver.find_element(By.ID, "gh-ac").send_keys(Keys.ENTER)
    search_field=self.driver.find_element(By.CSS_SELECTOR,"#srp-river-results > ul > li:nth-child(1) > div > div.s-item__info.clearfix > a > h3").text
    time.sleep(5)
    assert search_field =="Apple iPhone 11 64GB Factory Unlocked AT&T T-Mobile Verizon Very Good Condition"

  def test_testCase5_in_page(self):
    self.driver.get("https://www.ebay.com/")
    self.driver.set_window_size(1552, 840)
    element = self.driver.find_element(By.CSS_SELECTOR, "#mainContent > div.hl-cat-nav > ul > li:nth-child(3) > a")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "Apple").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".b-visualnav__tile:nth-child(1) .b-img").click()
    time.sleep(5)
    element = self.driver.find_element(By.CSS_SELECTOR, ".carousel__snap-point:nth-child(1) .b-img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".carousel__snap-point:nth-child(1) .b-img").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".x-item-title__mainTitle").click()
    time.sleep(5)
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .seo-breadcrumb-text > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "gh-ac").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR,"#gh-la").click()
    time.sleep(5)
    self.driver.find_element(By.ID, "gh-ac").send_keys("Apple iPhone 11 64GB Factory Unlocked AT&T T-Mobile Verizon Very Good Condition")
    self.driver.find_element(By.ID, "gh-ac").send_keys(Keys.ENTER)
    search_field=self.driver.find_element(By.CSS_SELECTOR,"#srp-river-results > ul > li:nth-child(1) > div > div.s-item__info.clearfix > a > h3")
    time.sleep(5)
    assert search_field.is_displayed()
