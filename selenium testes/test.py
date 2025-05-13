from django.test import TestCase

# Create your tests here.
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

class TestContato():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_contato(self):
    self.driver.get("http://localhost:5173/")
    self.driver.set_window_size(550, 692)
    self.driver.find_element(By.ID, "nome").click()
    self.driver.find_element(By.ID, "nome").send_keys("PabloRoberto")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("Pabloroberto")
    self.driver.find_element(By.ID, "telefone").click()
    self.driver.find_element(By.ID, "telefone").send_keys("testesdwasdasd")
    self.driver.find_element(By.ID, "mensagem").click()
    self.driver.find_element(By.ID, "mensagem").send_keys("To devendo um pix")
    self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()



  