#author	 :	PrabhakaranS
#purpose :	watches the crypto market and alerts when its time to buy
import requests
import json
from  collections import OrderedDict
import misound
import telePing
from time import sleep
import proxy

def coinwatch():
	f = open('buy.properties','r')
	pf = f.read()
	params = json.loads(pf,object_pairs_hook=OrderedDict)
	coins = params['coin']
	hval = 0
	wval = 0
	printdata = ''
	
	for k,v in coins.items():
		try :
			for ki,vi in v.items():
				url = 'https://api.bitfinex.com/v1/pubticker/'+ki+'usd'
				response = requests.request("GET", url)
				data =  json.loads(response.text)
				if (k == 'have'):
					hval = round(float(vi) * float(data['bid']),2)
					printdata = ki +': '+vi+' * '+data['bid'] + '='+str(hval)+' <> '
				else :
					wval = round(hval/float(data['ask']),2)
					printdata += ki +': '+vi+' * '+data['ask'] + '='+str(wval)+' <> '
					if wval >= float(vi):
						print('buy now.')
						misound.play()
						telePing.send(msg)
				
		except Exception as e:
			print('cant reach the network: ' +str(e))
	print('hval: '+str(hval) + ' wval: '+str(round(wval,2)))
	print(printdata)
while True:
	coinwatch()
	print('**********************')
	sleep(60)
# {
# "coin": {
# "have" : {"xlm": "35000"},
# "want" : {"btg": "203"},
# "want1" : {"etp": "3264"}
# }
# }
