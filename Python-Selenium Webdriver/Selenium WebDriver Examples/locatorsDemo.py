from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)

firstname = driver.find_element_by_id("Form_submitForm_FirstName")
lastname = driver.find_element_by_id("Form_submitForm_LastName")
e_mail = driver.find_element_by_id("Form_submitForm_Email")
NoOfEmp = driver.find_element_by_id("Form_submitForm_NoOfEmployees")
ComName = driver.find_element_by_id("Form_submitForm_CompanyName")
featurelink = driver.find_element_by_link_text("Features")


firstname.send_keys("Keshini")
lastname.send_keys("Patel")
e_mail.send_keys("kdpatel8184@gmail.com")
NoOfEmp.send_keys("134")
ComName.send_keys("k3d consulting")
time.sleep(10)

featurelink.click()



driver.quit()