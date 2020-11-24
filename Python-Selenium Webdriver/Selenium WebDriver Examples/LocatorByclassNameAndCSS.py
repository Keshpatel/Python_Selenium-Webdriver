from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(6)
driver.get("https://app.hubspot.com/login")



# username = driver.find_element_by_css_selector("#username")
# username = driver.find_element_by_class_name("login-email")
# username.send_keys("kdpatel8184@gmail.com")
# password = driver.find_element_by_css_selector("#password")
# password = driver.find_element_by_class_name("login-password")
# password.send_keys("Krupa2011")

# driver.find_element_by_class_name('login-submit').click()

# driver.find_element(By.CSS_SELECTOR, 'input.form-control.private-form__control.login-email').send_keys("kdpatel8184@gmail.com")

driver.find_element(By.LINK_TEXT, "Sign up").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Sign").click()