# -*- encoding: cp949 -*-

from data import parser
from ui import chart

if __name__ == "__main__":
    for coin_name in parser.coin_names():
        chart.show(parser.coin_candle_datas(coin_name, '30', '200'))
        break
