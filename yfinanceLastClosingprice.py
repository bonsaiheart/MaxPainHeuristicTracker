import pandas as pd
import yfinance as yf
import pandas
import datetime
from datetime import date
# def getlastClose(date):
#
#
#     tickerSymbol = 'SPY'
#     tickerData = yf.Ticker(tickerSymbol)
#     todayData = tickerData.history(close('2019-12-31'))
#     todayData['Close'][0]
#
#     print('datetime_object', datetime_object)
#     final_time = datetime_object + timedelta(minutes=15)
#     print('Final Time (15 minutes after given time ): ', final_time)
#     end_price = ticker.history(start=datetime_object, end=final_time, interval='1m')

def get_open_close_price(symbol):
    ticker = yf.Ticker(symbol)
    # dateneeded = date(2010, 12 , 3)
    stockHistory = ticker.history("max")
    # for x in stockHistory.index:
    #         stockHistory.index[x] = pd.to_datetime(stockHistory.index[x], format='%y/%m/%d').strftime("%m/%d/%y")
    print (type(stockHistory))
    print(stockHistory)
    print(type(stockHistory.index[1]))
    print(stockHistory.index[1])
    # a = datetime.date
    # print(stockHistory.loc[(12/28/22,1)])

    stockHistory.to_csv("stockhistory.csv")


get_open_close_price('TSLA')
print