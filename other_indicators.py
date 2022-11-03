import datetime
from datetime import date
import ephem
import talib
import pandas as pd
import numpy
import matplotlib.pyplot as plt

"""
0 - newmoon soon
1 - fullmoon soon
-1 - neutral moonphase 
"""

def moon():
    moon_buy = 0
    moon_sell = 0

    s = str(date.today()).split('-')
    mas = []
    for i in s:
        mas.append(int(i))
    ephem_date = ephem.Date(datetime.date(mas[0], mas[1], mas[2]))

    new_moon = ephem.next_new_moon(datetime.date(mas[0], mas[1], mas[2]))
    full_moon = ephem.next_full_moon(datetime.date(mas[0], mas[1], mas[2]))


    if ephem_date - full_moon < ephem_date - new_moon:
        if abs(ephem_date - full_moon) <= 3:
            return 1
    else:
        if abs(ephem_date - new_moon) <= 3:
            return 0
    return -1

def hash_ribbons():
    hash_data_link = "https://data.nasdaq.com/api/v3/datasets/BCHAIN/HRATE.csv?api_key=_ceSKrfy_fUJnxHD3DN9"
    df = pd.read_csv("BCHAIN-HRATE.csv")
    hash_values = []
    hash_dates = []

    for i in df["Value"]:
        hash_values.append(i)
    hash_values = hash_values[0:500]
    hash_values = hash_values[::-1]
    hash_values = numpy.array(hash_values)

    for i in df["Date"]:
        hash_dates.append(i)
    hash_dates = hash_dates[0:500]
    hash_dates = hash_dates[::-1]

    ma60 = talib.SMA(hash_values, timeperiod=60)
    ma30 = talib.SMA(hash_values, timeperiod=30)

    s1 = []
    for i in range(500):
        s1.append(i+1)

    plt.plot(s1, ma30, "-")
    plt.plot(s1, ma60, "*")

    buy_list = []
    idx = numpy.argwhere(numpy.diff(numpy.sign(ma30 - ma60))).flatten()
    for i in range(1,len(idx)):
        if ma30[idx[i]-1] < ma60[idx[i]-1]:
            buy_list.append(idx[i])

    return hash_dates[buy_list[-1]]


def btc_volatility():
    df = pd.read_csv("BTC-USD.csv")

    closes = []
    opens = []

    for i in df["Close"]:
        closes.append(i)
    for i in df["Open"]:
        opens.append(i)

    return abs((opens[-1] - closes[-1]))/closes[-1]*100

def Efficiency_Ratio():
    df = pd.read_csv("BTC-USD.csv")

    df['direction'] = df['Close'].diff(10).abs()
    df['volatility'] = df['Close'].rolling(10).sum()

    return (df['direction'][len(df['Close'])-1]/df['volatility'][len(df['Close'])-1])*100
