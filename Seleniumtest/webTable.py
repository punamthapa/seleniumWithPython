import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# count the number of rows and columns
noOfRows=len(driver.find_element(By.XPATH,"//table[@name='BookTable']//tr"))
# print(noOfRows)
#
noOfColumns=len(driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
# print(noOfColumns)


#read specific rows and column data
data =driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)

#read all the rows and column data
print("printing all the rows and columns data....")

for r in range(2,noOfRows+1):
    for c in range(1,noOfRows+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)