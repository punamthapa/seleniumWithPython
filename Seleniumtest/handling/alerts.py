import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# open alert window
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(5)

alertwindow =driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("welcome")
alertwindow.accept() #close alert window by using Ok button
alertwindow.dismiss() #close alert button by using cancel button
