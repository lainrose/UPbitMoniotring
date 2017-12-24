# -*- encoding: cp949 -*-

import json
import requests

"""
isTradingSuspended: False
code: 'CRIX.UPBIT.KRW-BTC'
exchange: 'UPBIT'
baseCurrencyCode: 'BTC' <가상화폐 통화 코드>
quoteCurrencyDecimalPlace: 0 <거래 가능 통화 코드>
koreanName: '비트코인' <화폐 한글 이름>
quoteCurrencyCode: 'KRW'
marketState: 'ACTIVE' <마켓 상태>
marketStateForIOS: 'ACTIVE'
timestamp: 1501485295000L
pair: 'BTC/KRW' <거래 단위>
englishName: 'Bitcoin' <화폐 영문 이름>
tradeStatus: 'ACTIVE'
baseCurrencyDecimalPlace: 8
"""
def coin_names():
    url = """https://s3.ap-northeast-2.amazonaws.com/crix-production/crix_master?nonce=1513815402981"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers).text
    js = json.loads(response)

    result = {}
    for coin_data in js:
        if coin_data['quoteCurrencyCode'] == u'KRW' and coin_data['marketState'] == u'ACTIVE':
            result[coin_data['baseCurrencyCode']] = coin_data['koreanName']
        else:
            continue

    return result


"""
code': CRIX.UPBIT.KRW-XEM' <코인 종류>
lowPrice': 1155.0
highPrice': 1225.0
candleDateTimeKst': 2017-12-19T15:00:00+09:00'
candleAccTradePrice': 3990655304.5082216
tradePrice': 1205.0
candleAccTradeVolume': 3348285.72026628
openingPrice': 1155.0'
candleDateTime': 2017-12-19T06:00:00+00:00
timestamp': 1513664991172L
unit': 30
"""
def coin_candle_datas(coin, time, count):
    if time in ['days', 'weeks', 'months']:
        url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/' + time
    else:
        url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/' + time

    params = {'code': 'CRIX.UPBIT.KRW-' + coin, 'count': count}
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, params=params, headers=headers).text
    js = json.loads(response)

    return js
