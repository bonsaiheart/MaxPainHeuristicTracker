
import openinterestapi as oi


tickerlist = open("Inputs/tickers_to_track.txt", "r")

for ticker in tickerlist.readlines():
    ticker = ticker.strip().upper()
    oi.retrive_oi_data(ticker)
    oi.write_oi_data_to_csv(ticker)
    oi.get_highest_oi_PC(ticker)


tickerlist.close()