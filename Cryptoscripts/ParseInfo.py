#! /usr/bin/python3

import json
import datetime
import collections
import matplotlib.pyplot as plt
import time

dataBtc = json.load(open('historyBtc.json'))#Open BtcHistory
dataEth = json.load(open('historyEth.json'))#Open EthHistory
dataLtc = json.load(open('historyLtc.json'))#Open LtcHistory

#initialize Ordered Dictionary
dictBtc = collections.OrderedDict()
dictEth = collections.OrderedDict()
dictLtc = collections.OrderedDict()
def parsehistory(): #Runs through the data received from the Api + builds dictionary for graphing.

	for i in range(len(dataEth["Data"])): #iterate through subdictionaries
		time  = dataEth["Data"][i]["time"] #get all values from key "time"
		close = dataEth["Data"][i]["close"] #get all values from key "close"
		convert = datetime.datetime.utcfromtimestamp(time).strftime('%m/%d/%y') #convert time from unix to UTC
		dictEth[convert] = close #join values

	for i in range(len(dataBtc["Data"])): #iterate through subdictionaries
		time  = dataBtc["Data"][i]["time"] #get all values from key "time"
		close = dataBtc["Data"][i]["close"] #get all values from key "close"
		convert = datetime.datetime.utcfromtimestamp(time).strftime('%m/%d/%y') #convert time from unix to UTC
		dictBtc[convert] = close #join values

	for i in range(len(dataLtc["Data"])): #iterate through subdictionaries
		time  = dataLtc["Data"][i]["time"] #get all values from key "time"
		close = dataLtc["Data"][i]["close"] #get all values from key "close"
		convert = datetime.datetime.utcfromtimestamp(time).strftime('%m/%d/%y') #convert time from unix to UTC
		dictLtc[convert] = close #join values

def graphbtc():
	datesBtc = list(dictBtc.keys())
	pricesBtc = list(dictBtc.values())
	datesBtc = [datetime.datetime.strptime(elem,'%m/%d/%y') for elem in datesBtc]
	plt.rcParams.update({'font.size': 6})
	plt.plot(datesBtc,pricesBtc, label='Bitcoin')
	plt.xlabel('Last 30 Days')
	plt.ylabel('Value in USD')
	plt.title('Bitcoin Value')
	plt.legend(loc='upper left')
	plt.savefig("/var/www/Front-End/BtcGraph.svg")
	plt.close()

def grapheth():
	datesEth = list(dictEth.keys())
	pricesEth = list(dictEth.values())
	datesEth = [datetime.datetime.strptime(elem,'%m/%d/%y') for elem in datesEth]
	plt.rcParams.update({'font.size': 6})
	plt.xlabel('Last 30 Days')
	plt.ylabel('Value in USD')
	plt.title('Ethereum Value')
	plt.plot(datesEth,pricesEth, label='Ethereum')
	plt.legend(loc='upper left')
	plt.savefig("/var/www/Front-End/EthGraph.svg")
	plt.close()

def graphltc():
	datesLtc = list(dictLtc.keys())
	pricesLtc = list(dictLtc.values())
	datesLtc = [datetime.datetime.strptime(elem,'%m/%d/%y') for elem in datesLtc]
	plt.rcParams.update({'font.size': 6})
	plt.xlabel('Last 30 Days')
	plt.ylabel('Value in USD')
	plt.title('LiteCoin Value')
	plt.plot(datesLtc,pricesLtc, label='LiteCoin')
	plt.legend(loc='upper left')
	plt.savefig("/var/www/Front-End/LtcGraph.svg")
	plt.close()

def graphEthLtc():
	datesEth = list(dictEth.keys())
	pricesEth = list(dictEth.values())
	datesLtc = list(dictLtc.keys())
	pricesLtc = list(dictLtc.values())
	datesEth = [datetime.datetime.strptime(elem,'%m/%d/%y') for elem in datesEth]
	datesLtc = [datetime.datetime.strptime(elem,'%m/%d/%y') for elem in datesLtc]
	plt.rcParams.update({'font.size': 6})
	plt.plot(datesEth,pricesEth, label='Ethereum')
	plt.xlabel('Last 30 Days')
	plt.ylabel('Value in USD')
	plt.title('Ethereum/Litecoin Value')
	plt.plot(datesLtc,pricesLtc, label='Litecoin')
	plt.legend(loc='upper left')
	plt.savefig("/var/www/Front-End/EthLtcGraph.svg")
	plt.close()
    
def graphEthBtc():
	datesBtc = list(dictBtc.keys())
	pricesBtc = list(dictBtc.values())

	datesEth = list(dictEth.keys())
	pricesEth = list(dictEth.values())

	datesBtc = [datetime.datetime.strptime(elem,'%m/%d/%y') for elem in datesBtc]
	datesEth = [datetime.datetime.strptime(elem,'%m/%d/%y') for elem in datesEth]

	plt.rcParams.update({'font.size': 6})
	plt.plot(datesBtc,pricesBtc, label='Bitcoin')
	plt.xlabel('Last 30 Days')
	plt.ylabel('Value in USD')
	plt.title('Bitcoin/Ethereum Value')
	plt.plot(datesEth,pricesEth, label='Ethereum')
	plt.legend(loc='upper left')
	plt.savefig("/var/www/Front-End/EthBtcGraph.svg")
	plt.close()
	return

