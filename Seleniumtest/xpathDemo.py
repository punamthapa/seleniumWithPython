import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

# absoulte xpath
# driver.find_element(By.XPATH , "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("Shirt")
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()
# time.sleep(5)

# relative xpath
# driver.find_element(By.XPATH , "//input[@id='search_query_top']").send_keys("Shirt")
# driver.find_element(By.XPATH, "//button[@name='submit_search']").click()
# time.sleep(5)

# or
# driver.find_element(By.XPATH , "//input[@id='search_query_top' or name='search_query']").send_keys("Shirt")
# driver.find_element(By.XPATH, "//button[@name='submit_search' or @class='btn btn-default button-search']").click()
# time.sleep(5)

# contains
# driver.find_element(By.XPATH , "//input[contains(@id,'search')]").send_keys("Shirt")
# driver.find_element(By.XPATH, "//button[starts-with(@name,'submit_')]").click()
# time.sleep(5)

# text
driver.find_element(By.XPATH,"//a[text()='Women']").click()
