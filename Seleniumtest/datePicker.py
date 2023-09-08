import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  #switch to frame

# mm/dd/yyyy
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("02/22/2024")

# time.sleep(5)

year="2024"
month="November"
day="19"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()  #open datepicker

while True:
    mon= driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/a[2]/span[1]").click()  #next arrow

time.sleep(5)