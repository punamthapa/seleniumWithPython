import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/docs/api/java/overview-summary.html")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/header[1]/nav[1]/div[1]/div[1]/ul[1]/li[8]").click()