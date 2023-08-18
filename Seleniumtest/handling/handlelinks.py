from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com")

# click on link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# find number of links in page
# using tag name
links = driver.find_elements(By.TAG_NAME,'a')
# using xpath
# links = driver.find_elements(By.XPATH,'//a')
print("Total number of links:", len(links))

# print all link text
for link in links:
    print(link.text)