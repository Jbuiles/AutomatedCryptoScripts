#!/usr/bin/python3
import urllib.request
import json 
import requests
import time
	
	#This line gets the price data for ETH,LTC,BTC from the API
	with urllib.request.urlopen("https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH,LTC,BTC&tsyms=USD") as url:
		data = json.loads(url.read().decode()) #Load the data to be referenced
		print(data)

	js = json.dumps(data)
	# Open json file to write to
	f = open('prices.json', 'w')
	
	# write to json file
	f.write(js)

	# close the connection
	f.close()
	time.sleep(120)
