from datetime import datetime
from bs4 import BeautifulSoup
import requests
import cloudscraper
import httpx
import wget

import pandas as pd


# scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# # Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
# print(scraper.get("http://somesite.com").text)  # => "<!DOCTYPE html><html><head>..."
# scraper = cloudscraper.create_scraper(browser={'browser': 'chrome','platform': 'windows','mobile': False})
# client = httpx.Client(http2=True)

# oipage = scraper.get("https://marketdata.theocc.com/series-search?symbolType=O&symbol=Spy")
# soup = BeautifulSoup(oipage.content, 'html.parser')
wget.download("https://marketdata.theocc.com/series-search?symbolType=O&symbol=Spy", "oidata.csv")

# print(soup)
# open("oidata").write(soup)



# for converting unix to date
# ts = int('1284101485')
#
# # if you encounter a "year is out of range" error the timestamp
# # may be in milliseconds, try `ts /= 1000` in that case
# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))