from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()