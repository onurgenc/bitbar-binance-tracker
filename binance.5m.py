#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>Binance Tracker</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Onur Genc</bitbar.author>
# <bitbar.author.github>onurgenc</bitbar.author.github>
# <bitbar.dependencies>python</bitbar.dependencies>
#

import json
import time
from datetime import datetime

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

print("💰")
print("---")

try:
	body = urlopen("https://api.binance.com/api/v1/ticker/24hr").read()
	obj = json.loads(body.decode('utf-8'))

	listUSDT = ['BTCUSDT','ETHUSDT','NEOUSDT','LTCUSDT']
	listBTC = ['KMDBTC','IOTABTC','BNBBTC','BCCBTC','XVGBTC','XLMBTC']
	list = listBTC + listUSDT
	up = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QAyQACAALwzISXAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACkSBTjB+AAAALNJREFUOMvVk70NAjEMhb87WYiGBZAQU7ABNSVSWpZgEEagsJDoKBELUCEKFuBuCKTw0xyQC0lICe5i+/k9/wT+3opUUJQhcAUqa8I5ZQT4tANwioGTCkQZA9vmOQE2oUJFhL0DXBz33RpKUfCLfLTQJMx9IlEWuQr6QB3prGtNS1lwiMvEYo7ekNsKRBkB+y+rH1hDFVOwy7ids+gbVzrsM6CXeYDTF85xroB1ZoHb73ymB5RhJkpZTihGAAAAAElFTkSuQmCC"
	down = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QABACnAADQ9FZaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACQ1FZwK3gAAAMRJREFUOMvNkjEKAjEQRZ+jKNjYKh5AbzCdjVcQj+BFPIKlp7EMeAJrUbASQVCEr80uG9cNbqe/Cgn/5WUI/DqNfBHM+kCzbs+lPUAr2pwBq5qABbB+M8gszkDvS/kOdAG5VBgEM4ApsP0CGLukjxlEoA0wSZR3Lo0qhxhZDIBDAmDA0wsBLD51CZeOwLKivHbprZx6AkAHuEXbD5fawYwywMqAzOKeDTTPvKqcTGZBMLsGs0utn5gADYEHcKp9e9ni//MCDtNCE3qjsIwAAAAASUVORK5CYII="

	for item in obj:
		if item['symbol'] in list:
			icon = up  if float(item['priceChangePercent']) > 0  else down
			link = "https://www.binance.com/trade.html?symbol="+item['symbol']
			
			if item['symbol'] in listUSDT:

				price = "{:.2f}".format(float(item['lastPrice']))	
				coin  = item['symbol'].replace('USDT','')
				print("{} ${} | image={} href={} dropdown=true".format(coin,price,icon,link))
			
			if item['symbol'] in listBTC:
				price = "{:.8f}".format(float(item['lastPrice']))	
				coin  = item['symbol'].replace('BTC','')
				print("{} {} | image= {} href={} ".format( coin,price,icon,link))
				
except:
	print("⚠️ unexpected error")

print("---")
print("Refresh | refresh=true")
