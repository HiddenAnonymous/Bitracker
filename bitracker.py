import requests
import json
from datetime import datetime
from urllib2 import urlopen
url="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"

#Define colors

G='\033[32m'
Y='\033[33m'
B='\033[34m'
response = urlopen(url)
data = json.load(response)
time = datetime.now().strftime("%I:%M:%S")
price=data['USD']

print(Y + '''
  ____  _ _            _       
 | __ )(_) |_ ___ ___ (_)_ __  
 |  _ \| | __/ __/ _ \| | '_ \ 
 | |_) | | || (_| (_) | | | | |
 |____/|_|\__\___\___/|_|_| |_|                              
''')

print(B + "Bitcoin price today")
print (B + "Live price: " + G +str (price)+"$")
print(B + "Time: " + B + time + "\n")

#By Hidden Anonymous