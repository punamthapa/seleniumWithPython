import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.opencart.com")
driver.find_element(By.XPATH,"//a[@class='btn btn-black navbar-btn']").click()

dropdownCountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

# select option
dropdownCountry.select_by_visible_text("Nepal")
# dropdownCountry.Select_by_value("10")
# dropdownCountry.Select_by_index(12)