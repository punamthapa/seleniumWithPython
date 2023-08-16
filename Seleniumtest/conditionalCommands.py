from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")

# is_displayed
# searchBox= driver.find_element(By.ID,"small-searchterms")
#
# print("Display status:", searchBox.is_displayed())
# print("Enable status:", searchBox.is_enabled())

# is_selected used for rardion/checkbox
rd_male = driver.find_element(By.ID,"gender-male")
rd_female = driver.find_element(By.ID,"gender-female")

print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()

print("After selecting male radio button....",rd_male.is_selected())
print(rd_female.is_selected())

driver.quit()