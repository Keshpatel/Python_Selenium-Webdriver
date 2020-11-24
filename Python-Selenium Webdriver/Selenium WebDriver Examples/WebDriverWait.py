from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login')


wait = WebDriverWait(driver, 10)
wait.until(ec.title_is('HubSpot Login'))
print(driver.title)

email_ele = wait.until(ec.presence_of_element_located((By.ID, 'username')))
email_ele.send_keys('kdpatel8184@gmail.com')
driver.find_element(By.ID, 'password').send_keys('pwd1234')

# driver.quit()