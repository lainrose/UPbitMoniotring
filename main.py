# -*- encoding: cp949 -*-

import json
import requests
"""
isTradingSuspended: False,
code: u'CRIX.UPBIT.KRW-BTC',
exchange: u'UPBIT',
baseCurrencyCode: u'BTC',
quoteCurrencyDecimalPlace: 0,
koreanName: u'�ube44�ud2b8�ucf54�uc778',
quoteCurrencyCode: u'KRW',
marketState: u'ACTIVE',
marketStateForIOS: u'ACTIVE',
timestamp: 1501485295000L,
pair: u'BTC/KRW',
englishName: u'Bitcoin',
tradeStatus: u'ACTIVE',
baseCurrencyDecimalPlace: 8
"""

def coin_datas():
    url = 'https://s3.ap-northeast-2.amazonaws.com/crix-production/crix_master?nonce=1513815402981'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers).text
    js = json.loads(response    )

    for data in js:
        print data['isTradingSuspended']

    return js

if __name__ == "__main__":
    coin_datas()

