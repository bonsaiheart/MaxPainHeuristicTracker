from datetime import datetime
from bs4 import BeautifulSoup
import requests
from pandas import pandas
import wget
from pathlib import Path
import pandas as pd
from datetime import date

today = pd.to_datetime(date.today()).strftime("%Y_%m_%d")


def retrive_oi_data(ticker):
    ticker = ticker.upper()
    output_dir = Path(f"tempdata/{ticker}")
    output_dir2 = Path(f"dataOutput/{ticker}_daily_OI")
    output_dir.mkdir(mode=0o755,parents=True, exist_ok=True)
    output_dir2.mkdir(mode=0o755,parents=True, exist_ok=True)
    wget.download(f"https://marketdata.theocc.com/series-search?symbolType=O&symbol={ticker}", f"tempdata/{ticker}/{today}_oi_dl.csv")

def write_oi_data_to_csv(ticker):
    ticker = ticker.upper()
    oicsv = pd.read_csv(f"tempdata/{ticker}/{today}_oi_dl.csv")
    oicsv.columns = oicsv.iloc[3]
    oicsv = oicsv.iloc[3:]

    oicsv.columns = ["ProductSymbol",	"year",	"Month",	"Day"	,"Integer"	,"Dec"	,"C/P"	,"Call",	"Put"	,"Position" ,"Limit"]


    oicsv.to_csv(f"dataOutput/{ticker}_daily_OI/{today}.csv")

def get_highest_oi_PC(ticker):
    df = pd.read_csv(f"dataOutput/{ticker}_daily_OI/{today}.csv")
    df["Period"] = df['year'].astype(str) + "-" + df["Duration"]
    print()

retrive_oi_data("ROKU")
write_oi_data_to_csv("roku")
### I want the highest OI put/call, max pain, ...

# for converting unix to date
# ts = int('1284101485')
#
# # if you encounter a "year is out of range" error the timestamp
# # may be in milliseconds, try `ts /= 1000` in that case
# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))