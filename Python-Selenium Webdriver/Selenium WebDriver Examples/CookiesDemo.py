from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
# print(driver.get_cookies())  # cookies in key and value format

# driver.delete_all_cookies()
print(len(driver.get_cookies()))  # printing length of the cookies

# driver.add_cookie({"name": "python", "domain": "reddit.com", "Value": "PythonSelenium"})  # adding cookies
# print(driver.get_cookies())

cookies = driver.get_cookies()

for cook_ele in cookies:
    print(cook_ele)

driver.quit()
