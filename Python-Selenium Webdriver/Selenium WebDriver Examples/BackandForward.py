from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.amazon.ca/')

driver.find_element(By.LINK_TEXT,'Best Sellers').click()

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.back()
time.sleep(3)
driver.refresh()

driver.quit()


