import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outerFrame= driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerFrame)

innerFrame= driver.find_element(By.XPATH,"iframe[src='SingleFrame.html']")
driver.switch_to.frame(innerFrame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")

time.sleep(10)