import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  #switch to frame

# mm/dd/yyyy
driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("02/22/2024")