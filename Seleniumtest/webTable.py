import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# count the number of rows and columns
noOfRows=len(driver.find_element(By.XPATH,"//table[@name='BookTable']//tr"))
print(noOfRows)

noOfColumns=len(driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(noOfColumns)