import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

# driver.find_element(By.ID, "login-input").send_keys("helloById@gmail.com")
# driver.find_element(By.NAME,"login-input").send_keys("helloByName@gmail.com")
# driver.find_element(By.XPATH,"/html//input[@id='login-input']").send_keys("xpath@gmail.com")
# driver.find_element(By.CLASS_NAME,"yt-sme-mobile-input ").send_keys("classname@gmail.com")
# time.sleep(5)



# Or
class demoFindElement():
    def locate_by_selector(self):
        driver.find_element(By.ID, "login-input").send_keys("helloById@gmail.com")
        # driver.find_element(By.NAME,"login-input").send_keys("helloByName@gmail.com")
        # driver.find_element(By.XPATH,"/html//input[@id='login-input']").send_keys("xpath@gmail.com")
        #driver.find_element(By.CLASS_NAME, "yt-sme-mobile-input ").send_keys("classname@gmail.com")
        time.sleep(5)
        driver.quit()

findBySelector =demoFindElement()
findBySelector.locate_by_selector()