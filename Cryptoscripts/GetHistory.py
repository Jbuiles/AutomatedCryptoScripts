import urllib.request
import json 
import requests
import time
#Get Historical Data ETH

def GetHistoricalEth():

	with urllib.request.urlopen("https://min-api.cryptocompare.com/data/histoday?fsym=ETH&tsym=USD&limit=30") as url:
		dataEth = json.loads(url.read().decode())
	js = json.dumps(dataEth)
	f = open('historyEth.json', 'w')
	f.write(js)
	f.close()
#Get Historical Data Btc
def GetHistoricalBtc():

	with urllib.request.urlopen("https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=30") as url:
		dataBtc = json.loads(url.read().decode())
	js = json.dumps(dataBtc)
	f = open('historyBtc.json', 'w')
	f.write(js)
	f.close()
#Get Historical Data Ltc
def GetHistoricalLtc():

	with urllib.request.urlopen("https://min-api.cryptocompare.com/data/histoday?fsym=LTC&tsym=USD&limit=30") as url:
		dataLtc = json.loads(url.read().decode())
	js = json.dumps(dataLtc)
	f = open('historyLtc.json', 'w')
	f.write(js)
	f.close()
