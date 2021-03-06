# Automated Crypto Scripts

# What is it?
These are a set of automated Python scripts that pulls pricing data from the cryptocurrency exchange site 
CryptoCompare(https://www.cryptocompare.com) via their supplied API and creates graphs to visualize price data.

# How does it work?
Using python, these scripts access the cryptocurrency exchange site via their API and extracts current cryptocurrency prices as well as historical data for individual crypto currencies. These Python scripts decode the data from the API and saves it as a json 
file locally on your system to be accessed by other scripts or for your own personal use. 
To be more precise, the GetHistory.py file gets the historical price data from the last 30 days for Ethereum, Litecoin and Bitcoin.
The GetPrices.py script gets the current market price for Ethereum, Litecoin and Bitcoin. The ParseInfo.py file is used to automatically generate a graph using the data received from Getprices.py and GetHistory.py

# What can it be used for?
These scripts can be used to automatically track cryptocurrency prices in real time and compare cryptocurrencies historically against one another over time. These scripts can be used as part of a Cryptocurrency exchange site, 
to make decisions to invest in certain cryptocurrencies or for your own personal cryptocurrency related projects.

# Note
These scripts are designed to be used on task scheduler for Windows or as a cronjob on Linux to automate the process of collecting data from the CryptoCompare api. These scripts can also be modified to get the price and historical data for any cryptocurrency currently listed on CryptoCompare. Included is an example of output from these scripts.

# Disclaimer
This is still a project in development. Code or features may change at any time.
