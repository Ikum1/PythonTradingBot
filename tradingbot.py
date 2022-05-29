from alpaca_trade_api.rest import REST, TimeFrame
import requests
import logging
from time import sleep
import pandas as pd

logging.basicConfig(
    filename = 'errlog.log',
    level = logging.WARNING,
    format='%(asctime)s:%(levelname)s:%message)s',
)

base_url = 'https://paper-api.alpaca.markets'
data_url = 'wss://data.alpaca.markets/v2'

api_key = 'PKJVSNLJZVAVRZUR6HLT'
api_secret = 'EiOEXPWcCyurIgFLus5BFLFkwdQdKVqH6HFt7JeM'

#instantiate rest api
api = REST(api_key, api_secret, base_url, api_version='v2')

# print (api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df)

api.submit_order(
    symbol='SPY',
    side='buy',
    type='market',
    qty='100',
    time_in_force='day',
    order_class='bracket',
    take_profit=dict(
        limit_price='420.0',
    ),
    stop_loss=dict(
        stop_price='400.5',
        limit_price='400.5',
    )
)

#request new order - post

#qty - 1
#symbol - amz
#side - buy

