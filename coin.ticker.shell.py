#author	 :	PrabhakaranS
#purpose :	utility for tracking crypto prices
import requests, json
from time import sleep

def getBitcoinPrice():
	coins = ['btc','btg','ltc','neo','etp','xlm']
	data = ''
	for coin in coins:
		
		url = 'https://api.bitfinex.com/v1/pubticker/'+coin+'usd'
		#print(url)
		
		
		try:
			r = requests.get(url)
			#print(r)
			price = float(json.loads(r.text)['last_price'])
			data += coin+': '+str(price)+' '
			#print(data)
		except requests.ConnectionError:
			print('Error querying Bitstamp API')
	return data
		
while True:
	print (str(getBitcoinPrice()))
	sleep(60) 
