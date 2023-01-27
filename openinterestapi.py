
import os
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
    if os.path.exists(f"tempdata/{ticker}/{today}_oi_dl.txt"):
        os.remove(f"tempdata/{ticker}/{today}_oi_dl.txt")
    if os.path.exists(f"tempdata/{ticker}/{today}_oi_dl_UNALTERED.txt"):
        os.remove(f"tempdata/{ticker}/{today}_oi_dl_UNALTERED.txt")
    wget.download(f"https://marketdata.theocc.com/series-search?symbolType=O&symbol={ticker}", f"tempdata/{ticker}/{today}_oi_dl.txt")
    wget.download(f"https://marketdata.theocc.com/series-search?symbolType=O&symbol={ticker}", f"tempdata/{ticker}/{today}_oi_dl_UNALTERED.txt")


def write_oi_data_to_csv(ticker):
    ticker = ticker.upper()
    with open(f"tempdata/{ticker}/{today}_oi_dl.txt", "r+") as infile:
        txt = infile.readlines()[6:]
        txt[0] = txt[0].replace("Position Limit", "PositionLimit")
        txt[0] = txt[0].replace("year", "Year")
        infile.seek(0)
        infile.writelines(txt)
        infile.truncate()

    with open(f"tempdata/{ticker}/{today}_oi_dl.txt", "r+") as infile:
        txt = infile.read().replace('\t\t','\t')
        infile.seek(0)
        infile.writelines(txt)
        infile.truncate()

    oicsv = pd.read_table(f"tempdata/{ticker}/{today}_oi_dl.txt")
    oicsv.drop(oicsv.columns[6], axis=1, inplace=True)
    oicsv.drop(oicsv.columns[8], axis=1, inplace=True)
    oicsv.drop(oicsv.columns[8], axis=1, inplace=True)
    oicsv.drop(oicsv.columns[0], axis=1, inplace=True)
    dec_as_float = oicsv["Dec"]
    float = dec_as_float/1000

    for value in oicsv["Integer"]:
        oicsv["Strike"] = oicsv["Integer"] + float
    oicsv.drop("Integer", axis=1, inplace=True)
    oicsv.drop("Dec", axis=1, inplace=True)
    oicsv['ExpDate'] = oicsv['Year'].astype(str) + oicsv['Month'].astype(str).str.zfill(2) + oicsv['Day'].astype(str).str.zfill(2)
    oicsv["ExpDate"] = pd.to_datetime(oicsv["ExpDate"], format="%Y%m%d")
    oicsv.drop(["Year"], axis=1,inplace=True)
    oicsv.drop(["Month"], axis=1,inplace=True)
    oicsv.drop(["Day"], axis=1,inplace=True)
    oicsv = oicsv.reindex(columns =["ExpDate","Strike","Call","Put"])
    oicsv.to_csv(f"dataOutput/{ticker}_daily_OI/{ticker}_{today}.csv",index_label="index")



def get_highest_oi_PC(ticker):
    ticker = ticker.upper()
    df = pd.read_csv(f"dataOutput/{ticker}_daily_OI/{ticker}_{today}.csv",index_col=["index"])
    print(df)
    calls_list = []
    highest_oi_calls_dict = {}
    puts_list = []
    highest_oi_puts_dict = {}

    for value in df["Call"]:
        calls_list.append(value)
    calls_list.sort(reverse=True)
    highcall_indexvalue = df[df['Call'] == calls_list[0]].index[0]
###TODO I think i want a chart taht has STRIKE, then above/below, the top OI.  There fore, I should probalby use lists instead of dicts.

    for value in df["Put"]:
        puts_list.append(value)
    puts_list.sort(reverse=True)
    highput_indexvalue = df[df['Put'] == puts_list[0]].index[0]



    for oi in calls_list[:5]:
        highcall_indexvalue = df[df['Call'] == oi].index[0]
        strike = df.at[highcall_indexvalue, "Strike"]
        highest_oi_calls_dict[oi] = strike

    for oi in puts_list[:5]:
        highput_indexvalue = df[df['Put'] == oi].index[0]
        strike = df.at[highput_indexvalue, "Strike"]
        highest_oi_puts_dict[oi] = strike


    print(f"Calls ={highest_oi_calls_dict}")
    print(f"Puts ={highest_oi_puts_dict}")
    output_dir = Path(f"dataOutput/{ticker}")
    output_dir.mkdir(mode=0o755,parents=True, exist_ok=True)

    #TODO make this write a datafrome, discover a suitable data vis. format.
    for key, value in highest_oi_calls_dict.items():
        df.loc[key] = value
        print(highest_oi_calls_dict)

    # with open(f"dataOutput/{ticker}/highest_oi_strikes.txt", "a") as outfile:
    #     calls_df = pd.DataFrame.from_dict(highest_oi_calls_dict)
    #     print(calls_df)
    #     puts_df = pd.DataFrame.from_dict(highest_oi_puts_dict)
    #     oi_df = pd.puts_df.concat(calls_df)
    #     outfile.write(oi_df)






#TODO collect OI data by "date fetched", collect into one file?