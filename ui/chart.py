# -*- encoding: cp949 -*-

import matplotlib
import matplotlib.finance as mpf
import matplotlib.dates as dates
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib as mpl
import pandas as pd
import pymssql
import datetime as dt
import numpy as np
from matplotlib.finance import candlestick_ohlc
from matplotlib import style


def show(candle_datas):
    style.use('fast')

    fig = plt.figure()
    ax = plt.subplot2grid((1, 1), (0, 0))
    ohlc = []
    for candle_data in candle_datas:
        print candle_data['candleDateTime']
        print candle_data['openingPrice'], candle_data['highPrice'], candle_data['lowPrice'], candle_data['tradePrice']
        stock_data = dates.date2num(dt.datetime.now()), candle_data['openingPrice'], candle_data['highPrice'], candle_data['lowPrice'], candle_data['tradePrice'],
        ohlc.append(stock_data)

    candlestick_ohlc(ax, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
    # ax.xaxis.set_major_locator(ticker.MaxNLocator(30))

    ax.set_title(candle_data['code'])
    #ax.set_ylabel('price')
    ax.grid()
    #ax.autoscale_view()

    #plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()
