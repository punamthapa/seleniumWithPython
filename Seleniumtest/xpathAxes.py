import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupall")

# self
# text_msg =driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/self::a").text
# print(text_msg)
# time.sleep(5)

# parent : since parent of this selector is td
text_msg =driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/parent::td").text
print(text_msg)
time.sleep(5)
