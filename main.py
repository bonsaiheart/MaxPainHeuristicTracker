import glob
from datetime import datetime
import pandas as pd
import operations
import matplotlib.pyplot as plt
import retrieve_mp_data
from pathlib import Path


ticker = input("Which ticker?").upper()

retrieve_mp_data.GetMaxPainData(ticker)

dailyCSVentries = glob.glob(f'dataOutput\\{ticker}_Daily_CSVs\\*.csv')

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

if today_datetime in listofmatchingdates:
    listofmatchingdates.remove(today_datetime)


def swap_backslash(i):
    x = i.replace('/', '-')
    return x


listofmatchingdates_backslash = [swap_backslash(i) for i in listofmatchingdates]
bigframe.index = pd.to_datetime(bigframe.index, format='%m/%d/%y').strftime("%m/%d/%y")
bigframe.columns = pd.to_datetime(bigframe.columns, format='%m/%d/%y').strftime("%m/%d/%y")
tickerhist = operations.RetrieveHistoricalData(f"{ticker}")


for a in listofmatchingdates_backslash:
    a = f"{a}"
    b = (datetime.strptime(a, '%Y-%m-%d').strftime("%m/%d/%y"))
    closingprice = '{:,.2f}'.format(tickerhist.get_closing_price(a))
    indexvalue = (bigframe.columns.get_loc(b)) + 1
    columnvalue = (bigframe.index.get_loc(b))
    bigframe.iat[columnvalue, indexvalue] = closingprice


output_dir = Path('dataOutput/')

output_dir.mkdir(parents=True, exist_ok=True)


bigframe.to_csv(f"dataoutput/{ticker}maxpain.csv")

bigframe = bigframe.astype(float)

chart1 = bigframe.plot(alpha=.3, loglog=False, lw=3, colormap='prism', marker='.', linestyle="dotted", markersize=10, title=f'{ticker} Heuristic staggered MaxPain')
chart1.set_xlabel("Exp. Date")
chart1.set_ylabel("Price $$$")


plt.legend(title="Date Gen.")
plt.show()
