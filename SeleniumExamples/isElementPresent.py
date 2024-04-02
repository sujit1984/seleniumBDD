import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# def is_element_present(id):
#     try:
#         driver.find_element(By.ID,id)
#         return True
#     except NoSuchElementException:
#         return False

def is_element_present(how, what):
    try:
        driver.find_element(by=how, value = what)
        return True
    except NoSuchElementException:
        return False


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.gmail.com")
driver.maximize_window()
driver.implicitly_wait(20)

# driver.find_element(By.ID, 'user-name').send_keys("standard_user")
# driver.find_element(By.ID, 'password').send_keys("secret_sauce")
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
# element.click()

#id_present = driver.find_element(By.ID,"identifierId111").is_displayed()
# print(is_element_present("identifierId111"))
print(is_element_present(By.ID,"identifierId112"))
#print(id_present)

time.sleep(5)
driver.quit()