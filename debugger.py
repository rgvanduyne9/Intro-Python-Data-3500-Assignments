import requests
import json
import time
from datetime import datetime, timedelta


# url =  "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=29-11-2023&localization=false"

url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

coins = ["bitcoin", "ethereum", "tether"]

dt = datetime(2022, 11, 29)

# dt = datetime(2022, 11, 29)

key1 = "market_data"

key2 = "current_price"

key3 = "usd"




for coin in coins: 
    file = open("/home/ubuntu/environment/Week14/" + coin + ".csv", "w")
    for i in range(3):
        dt += timedelta(days=1)
        
        
        dts = dt.strftime("%d-%m-%Y")
        # print(url1 + coin + url2 + dts + url3)
        url =url1 + coin + url2 + dts + url3
        request = requests.get(url)
        # time.sleep(6)
        request_dictionary = json.loads(request.text)
        
        file.write(dts + ", " + str(request_dictionary[key1][key2][key3]) + "\n")
        
    file.close()
        # next step
        # put info into a list
        # write lines into csv

















# request = requests.get(url)
# request_dictionary = json.loads(request.text)

# print(request_dictionary["market_data"]["current_price"]["usd"])

# market_data

# "current_price"

# "usd"

