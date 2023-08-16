from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
emailBox = driver.find_element(By.XPATH,"//input[@id='Email']")

emailBox.clear()
emailBox.send_keys("abc@gmail.com")

print("Result of text:",emailBox.text)
print("Result of getAttribute:",emailBox.get_attribute('value'))