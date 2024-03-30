import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://saucedemo.com")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.ID, 'user-name').send_keys("standard_user")
driver.find_element(By.ID, 'password').send_keys("secret_sauce")
WebDriverWait(driver, 10)
driver.find_element(By.ID, 'login-button').click()
time.sleep(5)
driver.quit()

