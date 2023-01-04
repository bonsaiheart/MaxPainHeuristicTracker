import glob
import os
from pathlib import Path
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
import chkMarketConditions
import operations
import matplotlib.pyplot as plt
import retrieve_mp_data


retrieve_mp_data

dailyCSVentries = glob.glob(r'dataOutput\SPY_Daily_CSVs\*.csv')

data = []


for csv in dailyCSVentries:
    df = pd.read_csv(csv)
    data.append(df)

bigframe = pd.concat(data, sort=False, ignore_index=True)
bigframe.set_index('maturitydate',  inplace=True)
bigframe.columns = pd.to_datetime(bigframe.columns, format='%m/%d/%y')
bigframe.index = pd.to_datetime(bigframe.index, format='%m/%d/%y')



bigframe = bigframe.reindex(sorted(bigframe.index))
bigframe = bigframe.transpose()
bigframe = bigframe.reindex(sorted(bigframe.index))


listofmatchingdates = [pd.to_datetime(c, format='%m/%d/%y').strftime("%Y/%m/%d") for c in bigframe.columns if c in bigframe.index]
today_datetime = datetime.today().strftime("%Y/%m/%d")
listofmatchingdates.remove(today_datetime)

def swapBackslashDash(i):
    x = i.replace('/', '-')
    return (x)

listofmatchingdateswithBackslash = [swapBackslashDash(i) for i in listofmatchingdates]
bigframe.index = pd.to_datetime(bigframe.index, format='%m/%d/%y').strftime("%m/%d/%y")
bigframe.columns = pd.to_datetime(bigframe.columns, format='%m/%d/%y').strftime("%m/%d/%y")






spy = operations.RetrieveHistoricalData("SPY")

for a in listofmatchingdateswithBackslash :
    a = f"{a}"
    b = (datetime.strptime(a,'%Y-%m-%d').strftime("%m/%d/%y"))

    closingprice = '{:,.2f}'.format(spy.populateClosingPrice(a))


    indexvalue = (bigframe.columns.get_loc(b)) + 1
    columnvalue = (bigframe.index.get_loc(b))

    bigframe.iat[columnvalue,indexvalue] = closingprice

bigframe.to_csv("dataoutput/maxpain.csv")

bigframe=bigframe.astype(float)
bigframe.info()
chart1 = bigframe.plot(alpha=.3, loglog=False, lw=3, colormap='prism', marker='.', linestyle="dotted",markersize=10, title='SPY Heuristic staggered MaxPain')
chart1.set_xlabel("Exp. Date")
chart1.set_ylabel("Price $$$")
print(bigframe.index)

plt.legend(title="Date Gen.")
plt.show()
bigframe = bigframe.fillna("n/a")