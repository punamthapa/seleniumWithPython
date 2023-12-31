import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.opencart.com")
driver.find_element(By.XPATH,"//a[@class='btn btn-black navbar-btn']").click()

dropdownCountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

# select option
# dropdownCountry.select_by_visible_text("Nepal")
# dropdownCountry.Select_by_value("10")
# dropdownCountry.Select_by_index(12)

# capture all the options and print them
alloptions =dropdownCountry.options
# print("total number of options",len(alloptions))
#
# for alloption in alloptions:
#     print(alloption.text)

# select option from dropdown without usong built-in method
for opt in alloptions:
    if opt.text=="Nepal":
        opt.click()
        break