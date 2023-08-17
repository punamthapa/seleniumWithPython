from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.implicitly_wait(10) #implicit wait in seconds

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys("selenium")
searchbox.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()