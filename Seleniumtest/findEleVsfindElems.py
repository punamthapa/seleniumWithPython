from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")

#find_element() -returns single webelement
# 1) locator matching with single webelement

# driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys("Apple macbook pro")

# 2)locator matching multiple elements

# element =driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)  #print first text from first link

# 3) if no element found --> then throws NoSuchElementException

# find_elements

# 1) locator matching with single webelement

# driver.find_elements(By.XPATH,"//input[@id='small-searchterms']").send_keys("Apple macbook pro")

# 2)locator matching multiple elements

element =driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(element[0].text)
for ele in element:
    print(ele.text)
# 3) if no element found --> then throws element available --> return 0


