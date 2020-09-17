import time

import requests
import schedule


def call_rest_api():
    resp = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()
    print(resp)
    # yield resp


schedule.every(1).seconds.do(call_rest_api)

while 1:
    schedule.run_pending()
    time.sleep(1)
