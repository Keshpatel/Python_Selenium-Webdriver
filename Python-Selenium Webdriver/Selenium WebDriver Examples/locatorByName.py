from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/")

print(driver.title)

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

login_button = driver.find_element_by_xpath("//input[@value='Login']")
username.send_keys("kdpatel8184@gmail.com")
password.send_keys("Krupa2011")

login_button.click()
driver.implicitly_wait(5)

driver.quit()