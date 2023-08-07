# import webdriver
from selenium import webdriver

# create webdriver object
# driver = webdriver.Firefox()
driver =webdriver.Chrome()
driver.maximize_window()
# get google.co.in
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("books")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.close()
