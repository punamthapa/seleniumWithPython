from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://itera-qa.azurewebsites.net/home/automation")

# 1) select specific checkbox
# driver.find_element(By.XPATH,"//ipnut[@id='monday]").click()

# 2) Select all the checkboxes
checkboxes = driver.find_element(By.XPATH,"//input[@type='checkbox',and contains(@id,'day')]")
# print(len(checkboxes))

# approach 1 to check box

# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# approarch 2:
# for checbox in checkboxes:
#     checbox.click()

# 3) select multiple checkboxes by choice
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute("id")
#     if weekname =="monday" or weekname=="sunday":
#         checkbox.click()

# 4) select last two checkboxes
#range(5,7) --> 6,7
#totalnumberofelelements-2=starting index
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()


