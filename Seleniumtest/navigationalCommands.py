import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/")
driver.back()
time.sleep(5)
driver.forward()  #amazon

driver.refresh()

driver.quit()