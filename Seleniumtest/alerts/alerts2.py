import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep()
myalert=driver.switch_to.alert
myalert.accept()