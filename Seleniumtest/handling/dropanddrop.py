import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://jqueryui.com/droppable/")
drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "draggable")))
drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "droppable")))
ActionChains(driver).drag_and_drop(drag, drop).perform()

# driver.refresh()
# source= driver.find_element(By.ID,"draggable")
# target= driver.find_element(By.ID,"droppable")
# action = ActionChains(driver)
# action.drag_and_drop(source, target).perform()
time.sleep(5)
driver.close()