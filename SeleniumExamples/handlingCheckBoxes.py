import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


def is_element_present(how, what):
    try:
        driver.find_element(by=how, value = what)
        return True
    except NoSuchElementException:
        return False
driver = webdriver.Chrome()
driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
driver.maximize_window()
driver.implicitly_wait(2)

# i=1
#
# while is_element_present(By.XPATH,"//div[4]/input["+str(i)+"]"):
#     driver.find_element(By.XPATH,"//div[4]/input["+str(i)+"]").click()
#     i+=1
#
# print("Total Check boxes are: ", i-1)

"""

Better Approach is given below 
"""
count =0
checkboxes = driver.find_elements(By.NAME,"sports")

for checkbox in checkboxes:
    checkbox.click()
    count+=1

print("Total Check boxes are: ", len(checkboxes))

