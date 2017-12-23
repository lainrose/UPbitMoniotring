# -*- encoding: cp949 -*-

import matplotlib
import matplotlib.finance as mpf
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib as mpl
import pandas as pd
import pymssql
import datetime as dt
import numpy as np
from matplotlib.finance import candlestick_ohlc


def show(candle_datas):
    #fig = plt.figure(figsize=(12, 8))
    #ax = fig.add_subplot(111)
    ax = plt.subplot2grid((1, 1), (0, 0))
    ohlc = []
    for candle_data in candle_datas:
        print candle_data['openingPrice'], candle_data['highPrice'], candle_data['lowPrice'], candle_data['tradePrice']
        stock_data = mdates.date2num(dt.datetime.now()), candle_data['openingPrice'], candle_data['highPrice'], candle_data['lowPrice'], candle_data['tradePrice'],
        ohlc.append(stock_data)

    candlestick_ohlc(ax, ohlc, width=0.5, colorup='r', colordown='b')
    ax.xaxis.set_major_locator(mticker.MaxNLocator(30))

    ax.set_title(candle_data['code'])
    #ax.set_ylabel('price')
    ax.grid()
    #ax.autoscale_view()

    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.show()
