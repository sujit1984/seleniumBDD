from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://way2automation.com")
driver.maximize_window()
title = driver.title

print(title)

assert "Selenium" in title