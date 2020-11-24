from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(15)
# time_out = 15
# dynamic wait
# implicit wait will be applied for all the web elements
# global wait
# for find_element and find_elements
# only for web_elements only
# not for non web element -> url , title, alert

driver.get("https://app.hubspot.com/login")

print(driver.title)
user_name = driver.find_element(By.ID, 'username')
user_name.send_keys("test@gmail.com")

driver.find_element(By.ID, 'password').send_keys("test@2011")
driver.find_element(By.ID, 'loginBtn').click()