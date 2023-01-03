import yfinance as yf

def getHistoryListStartWithOldest(symbol, earliestdateasstring):
    global stockHistory
    ticker = yf.Ticker(symbol)
    stockHistory = ticker.history(start=f""f"{earliestdateasstring}", end=f"2040-12-12", interval="1d")
    return stockHistory
    print(stockHistory)

getHistoryListStartWithOldest("spy")
#  working on appending cell data from close   # for x in listofmatchingdatesAsSTRINGS:
#     #     x = dat
    #     bigframe.loc[2,x] = stockHistory.at[f"{x}", 'Close']
def retrieveActualClose(closedate):
    close =

