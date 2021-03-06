from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('http://londonfreelance.org/courses/frames/index.html')

# driver.switch_to.frame("main")   # By name
# driver.switch_to.frame(2)  #by frame number

frame_ele = driver.find_element(By.NAME, 'main')
driver.switch_to.frame(frame_ele)
headerValue = driver.find_element(By.CSS_SELECTOR, 'body > h2').text
print(headerValue)

# driver.switch_to.default_content()
# driver.switch_to.parent_frame()