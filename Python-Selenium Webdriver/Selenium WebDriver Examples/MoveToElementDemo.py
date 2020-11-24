from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.spicejet.com/')
time.sleep(3)

'''Move to Element'''
login_ele = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
action_chain = ActionChains(driver)
action_chain.move_to_element(login_ele).perform()

spice_club_ele = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
action_chain.move_to_element(spice_club_ele).perform()
# spice_club_ele.click()

member_login = driver.find_element(By.LINK_TEXT, 'Member Login')
member_login.click()

time.sleep(3)
driver.quit()


