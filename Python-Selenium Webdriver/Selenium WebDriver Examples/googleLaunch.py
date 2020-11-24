from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.headless = True            # Make it False for running in hadless mode
driver = webdriver.Chrome(executable_path="C:\\Users\\Keshini\\PycharmProjects\\Python-Selenium-Demo-By-Keshini\\SeleniumSessions\\Drivers\\chromedriver.exe", options=options)
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
title = driver.title
print(title)

driver.find_element_by_name('q').send_keys("naveen automationlabs")
optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(optionsList))

for el in optionsList:
    print(el.text)
    if el.text == 'naveen automationlabs youtube':
        el.click()
        break

time.sleep(5)
driver.quit()

