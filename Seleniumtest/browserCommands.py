import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://orangehrm.qedgetech.com/symfony/web/index.php/auth/login")

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

time.sleep(5)

# driver.close()
driver.quit()