import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
driver.implicitly_wait(20)

# driver.find_element(By.ID, 'user-name').send_keys("standard_user")
# driver.find_element(By.ID, 'password').send_keys("secret_sauce")
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
# element.click()

lang_select = driver.find_element(By.ID, "searchLanguage")
select = Select(lang_select)
#select.select_by_visible_text("Eesti")
select.select_by_value("hi")
lang_options = driver.find_elements(By.TAG_NAME,'option')
#count = 0
for lang in lang_options:
    #count+=1
    print("Text is: ", lang.text, "Language code: " +lang.get_attribute("lang"))
print("Total languages are ", len(lang_options))
print("------------Printing all the Links-------------------")

links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print("The link is: ", link.text, "and the Url is: ", link.get_attribute("href"))

print(len(links))

"""
Find links only in a particular section of the page
"""
block = driver.find_element(By.XPATH,"//*[@id=\"www-wikipedia-org\"]/footer/nav")
block_links = block.find_elements(By.TAG_NAME,"a")

for block_link in block_links:
    print("Text is: ", block_link.text, "Url is:", block_link.get_attribute("href"))

print(len(block_links))

"""
Getting the first item from the block of links 

"""

print("1st link is: ", block.find_elements(By.TAG_NAME,"a").__getitem__(0).text)



time.sleep(5)
driver.quit()