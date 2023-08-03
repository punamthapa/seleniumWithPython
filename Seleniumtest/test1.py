# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Firefox()
# driver =webdriver.Chrome()

# get google.co.in
driver.get("https://google.com")