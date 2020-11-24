from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time


browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('please pass the correct browser name' + browserName)
    raise Exception("Driver not found")

driver.get("https://freecrm.com/")

title = driver.title

print(title)

driver.find_element_by_xpath("//span[text()='Log In']").click()
driver.implicitly_wait(5)
driver.find_element_by_name("email").send_keys("kdpatel8184@gmail.com")
driver.find_element_by_name("password").send_keys("Krupa2011")
driver.find_element_by_xpath("//div[text()='Login']").click()

time.sleep(5)

driver.quit()


time.sleep(5)
driver.quit()
