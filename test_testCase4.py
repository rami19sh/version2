# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as FirefoxService

class TestTestCase4():
  def setup_method(self, method):
    browser_name = "firefox"

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
  
  def test_testCase4_all_incorrect_values (self):
    self.driver.get("https://www.ebay.com/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.LINK_TEXT, "register").click()
    self.driver.find_element(By.ID, "firstname").click()
    self.driver.find_element(By.ID, "firstname").send_keys("hdg2324@$%")
    self.driver.find_element(By.ID, "lastname").send_keys("@$$shd636")
    self.driver.find_element(By.ID, "Email").send_keys("shfg.sjfh4")
    self.driver.find_element(By.ID, "password").send_keys("sdjkdfdkjf376373")
    time.sleep(5)
    email_error_msg=self.driver.find_element(By.CSS_SELECTOR,"#Email_err").text
    expected_msg="Email address is invalid. Please enter a valid email address."
    create_account_btn_html='"<button name="EMAIL_REG_FORM_SUBMIT" id="EMAIL_REG_FORM_SUBMIT" class="btn btn--primary btn--large btn--fluid" disabled="" type="submit" aria-describedby="legalTextId" data-click-tracking-data="{&quot;linkId&quot;:47252,&quot;pageId&quot;:&quot;2560839&quot;,&quot;type&quot;:&quot;_plsr&quot;,&quot;payload&quot;:{&quot;RegModuleName&quot;:&quot;PARTIAL_REG_PERSONAL_EMAIL&quot;,&quot;bs&quot;:206,&quot;ul&quot;:&quot;en-US&quot;,&quot;uc&quot;:100}}">Create account</button>"'
    assert "disabled" in create_account_btn_html
    assert email_error_msg==expected_msg


  def test_testCase4_incorrect_first_last_name (self):
    self.driver.get("https://www.ebay.com/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.LINK_TEXT, "register").click()
    self.driver.find_element(By.ID, "firstname").click()
    first_name="hdg$2324"
    self.driver.find_element(By.ID, "firstname").send_keys(first_name)
    self.driver.find_element(By.ID, "lastname").send_keys("@$$shd636")
    self.driver.find_element(By.ID, "Email").send_keys("ralofoh333@tagbert.com")
    self.driver.find_element(By.ID, "password").send_keys("sdjkdfdkjf376373")
    time.sleep(5)
    self.driver.find_element(By.ID, "EMAIL_REG_FORM_SUBMIT").click()
    try:
      time.sleep(5)
      profile_name = self.driver.find_element(By.CSS_SELECTOR, "b:nth-child(1)").text
      time.sleep(5)
      assert first_name== profile_name
    except NoSuchElementException:
      print("\nno such element")


  def test_testCase4_incorrect_first_last_name2 (self):
    self.driver.get("https://www.ebay.com/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.LINK_TEXT, "register").click()
    self.driver.find_element(By.ID, "firstname").click()
    first_name="hdg$2*(%324"
    self.driver.find_element(By.ID, "firstname").send_keys(first_name)
    self.driver.find_element(By.ID, "lastname").send_keys("@$$shd636")
    self.driver.find_element(By.ID, "Email").send_keys("temos35844@runqx.com")
    self.driver.find_element(By.ID, "password").send_keys("sdjkdfdkjf376373")
    time.sleep(5)
    self.driver.find_element(By.ID, "EMAIL_REG_FORM_SUBMIT").click()
    time.sleep(5)
    profile_name = self.driver.find_element(By.CSS_SELECTOR, "b:nth-child(1)").text
    time.sleep(10)
    first_name_error_msg = self.driver.find_element(By.CSS_SELECTOR, "#firstname_err")
    assert "Please enter a valid name."==first_name_error_msg.text

  #Ebay allows digits and signs with a first name and last name but does not approve all the signs
