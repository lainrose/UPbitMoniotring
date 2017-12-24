# -*- encoding: cp949 -*-

from data import parser
from ui import chart

if __name__ == "__main__":
    for coin_name in parser.coin_names():
        if coin_name == 'MER':
            chart.show(parser.coin_candle_datas(coin_name, 'days', '500'))
            break
