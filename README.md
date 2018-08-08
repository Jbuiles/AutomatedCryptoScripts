# Automated Crypto Scripts

# What is it?
These are a set of automated Python scripts that pull data from the cryptocurrency exchange site 
CryptoCompare(https://www.cryptocompare.com) via their supplied API. 

# How does it work?
Using python, these scripts access the cryptocurrency exchange site via their API and extracts current cryptocurrency prices as well as historical data for individual crypto currencies. These Python scripts decode the data from the API and saves it as a json 
file locally on your system to be accessed by other scripts or for your own personal use. 
To be more precise, the GetHistory.py file gets the historical price data from the last 30 days for Ethereum, Litecoin and Bitcoin.
The GetPrices.py script gets the current market price for Ethereum, Litecoin and Bitcoin. These scripts can be used on 
task scheduler for Windows to automate the process of collecting this data or by setting a cronjob in Linux environments to do the same. These scripts can be modified to get the price data for any cryptocurrency currently listed on CryptoCompare.

# What can it be used for?
These scripts can be used to automatically track cryptocurrency prices in real time and compare cryptocurrencies historically against one another over time. These scripts can be used as part of a Cryptocurrency exchange site, 
to make decisions to invest in certain cryptocurrencies or for your own personal cryptocurrency related projects.
