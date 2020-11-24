from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.freshworks.com/")


linkList = driver.find_elements(By.TAG_NAME, 'a')
print("Total link available on page is :: ", len(linkList))

for ele in linkList:
    link_text = ele.text
    print(link_text)
    print(ele.get_attribute('href'))


imagesList = driver.find_elements(By.TAG_NAME, 'img')
print(len(imagesList))

for ele in imagesList:
    print(ele.get_attribute('src'))