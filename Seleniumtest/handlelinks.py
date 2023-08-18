from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com")

# click on link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# find number of links in page
links = driver.find_elements(By.TAG_NAME,'a')
print("Total number of links:", len(links))