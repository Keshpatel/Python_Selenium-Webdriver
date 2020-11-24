from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")


def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)


def select_value_dropdown(dropdownOptionsList, value):
    print(len(dropdownOptionsList))
    for ele in dropdownOptionsList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break


def get_options(dropdownOptionsList):
    print("Industry Options: ", len(dropdownOptionsList))
    for ele in dropdownOptionsList:
        print(ele.text)


indus_options = driver.find_elements(By.XPATH, '//select [@id ="Form_submitForm_Industry"]/option')
select_value_dropdown(indus_options, 'Education')
select_value_dropdown(indus_options, 'Travel')


get_options(indus_options)

ele_No_Of_Emp = driver.find_element(By.ID, 'Form_submitForm_NoOfEmployees')
ele_industry = driver.find_element(By.ID, 'Form_submitForm_Industry')
ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')

select_values(ele_industry, 'Education')
select_values(ele_country, 'India')

# ************Without Generic method code**********************

# select_NoOfEmp = Select(ele_No_Of_Emp)
# select_NoOfEmp.select_by_value('151 - 200')

# select_industry = Select(ele_industry)
# select_industry.select_by_index(6)

#select_country = Select(ele_country)
# select_country.select_by_visible_text('Canada')

# print(Select.is_multiple)

# Printing all the values from DropDown using Select Class

# select = Select(ele_industry)
# industry_list = select.options
# for ele in industry_list:
#   print(ele.text)
#   if(ele.text == 'Automotive'):
#        ele.click()
#        break

# without select class Printing all the values from DropDown
# print(len(indus_options))
# for ele in indus_options:
#    print(ele.text)
#    if ele.text == 'Travel':
#        ele.click()
#        break




