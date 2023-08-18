import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")

# brokenlinks - the link which doesnot have any target page
# install request module first
# goto files > settings > project name -> python interpeter ->click on + >type requests -> install packages

links= driver.find_elements(By.TAG_NAME,"a")
print(len(links))
count = 0
for link in links:
    url = link.get_attribute("href")
    try:
     res=requests.head(url)
    except:
        None
    if res.status_code >=400:
        print(url," is broken link")
        count+=1
    else:
        print(url,"valid link")

print("The total broken link ",count)


