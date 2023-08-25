import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
windowId= driver.current_window_handle

print(windowId)

driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(5)
windowIds=driver.window_handles


# approach 1
# parentId=windowIds[0]  #will give same as first one
# childId =windowIds[1]
# print(childId)
#
# driver.switch_to.window(childId)
# print(driver.title)
#
# driver.switch_to.window(parentId)
# print(driver.title)

# approach 2

for windid in windowIds:
    driver.switch_to.window(windid)
    if driver.title=="OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM" or driver.title =="XYZ":
        driver.close()