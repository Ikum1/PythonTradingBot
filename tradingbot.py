from alpaca_trade_api.rest import REST, TimeFrame, stream2
import requests
import logging
from time import sleep
import pandas as pd

logging.basicConfig(
    filename = 'errlog.log',
    level = logging.WARNING,
    format='%(asctime)s:%(levelname)s:%message)s',
)


domain = 'https://paper-api.alpaca.markets'
keyID = 'PKJVSNLJZVAVRZUR6HLT'
secretKey = 'EiOEXPWcCyurIgFLus5BFLFkwdQdKVqH6HFt7JeM'

api = REST(keyID, secretKey, domain, api_version='v2')

print (api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df)


