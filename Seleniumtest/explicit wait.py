from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import invisibility_of_element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# driver-> specified driver, 10-> cutout time, maximum time
# mywait = WebDriverWait (driver,10) #explicit wait declaration

# we can specify the exceptions to ignore
# mywait = WebDriverWait (driver,10,ignored_exceptions=[NoSuchElementException,
#                                                       invisibility_of_element,
#                                                       Exception])

# poll frequency-> for every 2 seconds for 5 times (2*5=10) it will poll/search for element
mywait = WebDriverWait (driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,invisibility_of_element,Exception])

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys("selenium")
searchbox.submit()

# initializating with conditions
searchLink = mywait.until(EC.presence_of_element_located(By.XPATH,"//h3[text()='Selenium']"))
searchLink.click()
