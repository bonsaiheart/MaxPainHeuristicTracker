import numpy
import requests
import lxml
import yfinance as yf
import csv

spy = yf.Ticker("SPY")

# get stock info
# spy.info
#
# # get historical market data
# # hist = spy.history(period="max")
#
# # show actions (dividends, splits)
# spy.actions

# # show dividends
# spy.dividends

# # show splits
# spy.splits

# show financials
spy.financials
spy.quarterly_financials

# show major holders
spy.major_holders

# show institutional holders
spy.institutional_holders

# # show balance sheet
# spy.balance_sheet
# spy.quarterly_balance_sheet

# show cashflow
# spy.cashflow
# spy.quarterly_cashflow
#
# # show earnings
# spy.earnings
# spy.quarterly_earnings
#
# # # show sustainability
# spy.sustainability
#
# # show analysts recommendations
# spy.recommendations
#
# # show next event (earnings, etc)
# spy.calendar
#
# # show all earnings dates
# spy.earnings_dates
#
# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# spy.isin

# show options expirations
print(spy.options)

# show news
# print(spy.news)

# # get option chain for specific expiration
opt = spy.option_chain('2022-10-17')
# # data available via: opt.calls, opt.puts



# open the file in the write mode
with open('optiondata', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(opt)

