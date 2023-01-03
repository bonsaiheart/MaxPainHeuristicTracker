import glob
import os
from pathlib import Path
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
import chkMarketConditions
import operations

# dailyCSVentries = glob.glob(r'dataOutput\SPY_Daily_CSVs\*.csv')
#
# data = []
#
# for csv in dailyCSVentries:
#     df = pd.read_csv(csv)
#     data.append(df)
#
# bigframe = pd.concat(data, sort=False, ignore_index=True)
# bigframe.set_index('maturitydate',  inplace=True)
# bigframe.columns = pd.to_datetime(bigframe.columns, format='%m/%d/%y')
# bigframe.index = pd.to_datetime(bigframe.index, format='%m/%d/%y')
# # bigframe.columns = bigframe.columns.sort_values(ascending=False)
# # bigframe.index = bigframe.index.sort_values(ascending=False)
#
# bigframe = bigframe.reindex(sorted(bigframe.index))
# bigframe = bigframe.transpose()
# bigframe = bigframe.reindex(sorted(bigframe.index))
#
#
# listofmatchingdates = [pd.to_datetime(c, format='%m/%d/%y').strftime("%Y/%m/%d") for c in bigframe.columns if c in bigframe.index]
# def changeDatestoStrings(i):
#     x = i.replace('/', '-')
#     return str(x)
#
# listofmatchingdatesAsSTRINGS = [changeDatestoStrings(i) for i in listofmatchingdates]
# bigframe.index = pd.to_datetime(bigframe.index, format='%m/%d/%y').strftime("%m/%d/%y")
# bigframe.columns = pd.to_datetime(bigframe.columns, format='%m/%d/%y').strftime("%m/%d/%y")
#
# bigframe = bigframe.fillna("N/A")
#
#


getHistoryListStartWithOldest("spy", listofmatchingdatesAsSTRINGS[0])

bigframe.to_csv("dataoutput/maxpain.csv")