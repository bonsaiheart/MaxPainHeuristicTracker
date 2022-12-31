import glob
import os
from pathlib import Path
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

dailyCSVentries = glob.glob(r'dataOutput\SPY_Daily_CSVs\*.csv')

data = []

for csv in dailyCSVentries:
    df = pd.read_csv(csv)
    columns = df.columns
    data.append(df)

bigframe = pd.concat(data, ignore_index=False) #dont want align row indexes
bigframe.set_index('maturitydate',  inplace=True)
bigframe.columns = pd.to_datetime(bigframe.columns, format='%m/%d/%y')
bigframe = bigframe[sorted(bigframe.columns)]

bigframe = bigframe.fillna("N/A")
bigframe = bigframe.transpose()

listofmatchingdates = [pd.to_datetime(c, format='%m/%d/%y').strftime("%Y/%m/%d") for c in bigframe.columns if c in bigframe.index]
def changeDatestoStrings(i):
    x = i.replace('/', '-')
    return str(x)


listofmatchingdatesAsSTRINGS = [changeDatestoStrings(i) for i in listofmatchingdates]


bigframe.index = pd.to_datetime(bigframe.index, format='%m/%d/%y').strftime("%m/%d/%y")
bigframe.columns = pd.to_datetime(bigframe.columns, format='%m/%d/%y').strftime("%m/%d/%y")

stockHistory = 1
def getHistoryListStartWithOldest(symbol):
    global stockHistory
    a = listofmatchingdatesAsSTRINGS[0]
    ticker = yf.Ticker(symbol)
    stockHistory = ticker.history(start=f"{a}", end=f"2030-12-12", interval="1d")
    for a in listofmatchingdatesAsSTRINGS:
        stockHistory.at[f"{a}", 'Close']



bigframe.to_csv("dataoutput/maxpain.csv")
