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
# text_msg =driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/parent::td").text
# print(text_msg)
# time.sleep(5)

# child : since td has no child, so we went to ancestor tr and get its child
# childs = driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/child::td")
# print(len(childs))
# time.sleep(5)

# ancestor
# text_msg =driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr").text
# print(text_msg)

# descendent
text_msg =driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/descendant::*")
print(len(text_msg))
driver.close()