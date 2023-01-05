import csv
from datetime import date, timedelta
import pandas as pd
import chkMarketConditions
from IPython.display import display
import pandas_market_calendars as mcal
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import webdriver_manager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


## options = Options()
## options.binary_location = r'C:\Program Files (x86)\Mozilla Firefox'
## driver = webdriver.Firefox()
## # for trouble getting geckodriver working
## webdriver-
## driver = webdriver.Firefox(service=(Gecko().install()))

global error
error = 0

chkMrkt = chkMarketConditions.MarketCondition("george")
chkMrkt.is_market_open_today()
if chkMrkt.is_market_open_today() == False:
    print("Market Closed")
    exit()

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://maximum-pain.com/options/SPY')
element_dropdown = driver.find_element(By.TAG_NAME, "select")
all_options = element_dropdown.find_elements(By.TAG_NAME, "option")
a = ((By.XPATH, "/html/body/app-root/div/div[1]/div/app-options/div/div[8]/div/app-straddle/table/caption/b"))
b = By.TAG_NAME, "app-maxpain"
c = By.XPATH, "/html/body/app-root/div/div[1]/div/app-options/div/div[4]/div/app-chart/div/div[2]/div[2]/label/input"
htmlDateGeneratedline = By.XPATH, "/html/body/app-root/div/div[1]/div/app-options/div/div[3]/div/app-summary/table/tbody/tr/td[1]"
dateGenerated1 = driver.find_element(By.XPATH, "/html/body/app-root/div/div[1]/div/app-options/div/div[3]/div/app-summary/table/tbody/tr/td[1]").get_attribute("innerHTML")
dateGenerated = pd.to_datetime(dateGenerated1, infer_datetime_format='%m/%d/%y').strftime("%m/%d/%y")
repeat_date_check_list = [0]
data_list = []
data_dict = {"maturitydate": dateGenerated}
todayinweirdformat = date.today()
today = pd.to_datetime(todayinweirdformat, infer_datetime_format='%m/%d/%y').strftime("%m-%d-%y")
todayasYYMMDD = todayinweirdformat.strftime("%Y_%m_%d")



for option in all_options:
    option.click()
    #website posts as mm/dd/yyyy, need to convert so it parses correctly when concatenated in pandas later.
    maturitydate1 = driver.find_element(By.XPATH, "/html/body/app-root/div/div[1]/div/app-options/div/div[10]/div/app-maxpain/table/caption/b[1]").get_attribute("innerHTML").removeprefix("SPY maturity ")
    maturitydate = pd.to_datetime(maturitydate1, infer_datetime_format='%m/%d/%y').strftime("%m/%d/%y")


    if maturitydate != repeat_date_check_list[-1]:
        maxpainstring = (driver.find_element(By.XPATH,  "/html/body/app-root/div/div[1]/div/app-options/div/div[10]/div/app-maxpain/table/caption/b[2]").get_attribute("innerHTML")).removeprefix("Max Pain $")
        maxpain = '{:,.2f}'.format(float(maxpainstring))
        print(maxpain)
        data_list.append(maxpain)
        data_dict[maturitydate] = maxpain
        repeat_date_check_list.append(maturitydate)
        print(maxpain)
    else:
        print("Error: Webdriver has timed out.")
        data_dict = ""
        today = f"Timeout Error {today}"
        error = 1
driver.close()
print(data_dict)
if error == 0:
    with open(f"dataOutput/SPY_Daily_CSVs/{todayasYYMMDD} SPY MaxPain.csv", 'w') as file:
        writer = csv.DictWriter(file, data_dict.keys())
        writer.writeheader()
        writer.writerow(data_dict)
