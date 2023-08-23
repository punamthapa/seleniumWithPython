import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# https://the-internet.herokuapp.com/basic_auth
driver.get("https://admin@admin:the-internet.herokuapp.com/basic_auth")

time.sleep(5)