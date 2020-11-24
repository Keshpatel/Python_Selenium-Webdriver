from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(executable_path="C:\\Users\\Keshini\\PycharmProjects\\Python-Selenium Webdriver\\Drivers\\chromedriver.exe", options=options)
driver.implicitly_wait(5)
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

