import time

from selenium import webdriver
import custom_wait_cond
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://maximum-pain.com/options/SPY')

element_dropdown = driver.find_element(By.TAG_NAME, "select")

repeat_date_check_list = [0]
data_list = []
all_options = element_dropdown.find_elements(By.TAG_NAME, "option")
a = ((By.XPATH, "/html/body/app-root/div/div[1]/div/app-options/div/div[10]/div/app-maxpain/table/caption/b[2]"))
b = By.TAG_NAME, "app-maxpain"
c= By.XPATH, "/html/body/app-root/div/div[1]/div/app-options/div/div[4]/div/app-chart/div/div[2]/div[2]/label/input"
for option in all_options:
    maturitydate = driver.find_element(By.XPATH, "/html/body/app-root/div/div[1]/div/app-options/div/div[10]/div/app-maxpain/table/caption/b[1]").get_attribute(
        "innerHTML")
    while maturitydate != repeat_date_check_list[-1]:
        # time.sleep(.3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(a))
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(c))

        if maturitydate != repeat_date_check_list[-1]:
            maxpain = str(driver.find_element(By.XPATH, "/html/body/app-root/div/div[1]/div/app-options/div/div[10]/div/app-maxpain/table/caption/b[2]").get_attribute("innerHTML"))
            data_list.append(maxpain)
            repeat_date_check_list.append(maturitydate)
            continue
        else:
            print("error, webdriver timed out and may not have collected all info.")
        option.click()
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(b))
print(data_list)
print(maturitydate)

