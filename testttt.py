# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WebDriver Chrome
driver = webdriver.Chrome()

# Target URL
driver.get("https://www.theocc.com/mdapi/series-search?symbol_type=O&symbol=Spy&exchange=")
time.sleep(5)


print(driver.find_element(By.XPATH, "/html/body").text)


driver.close()