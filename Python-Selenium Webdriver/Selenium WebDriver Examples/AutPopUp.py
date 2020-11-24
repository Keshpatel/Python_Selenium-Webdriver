from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

time.sleep(3)

driver.quit()