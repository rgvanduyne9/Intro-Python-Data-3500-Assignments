import requests
import json
import time
from datetime import datetime, timedelta


# url =  "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=29-11-2023&localization=false"

def initial_data_pull(coins):
    url1 = "https://api.coingecko.com/api/v3/coins/"
    url2 = "/history?date="
    url3 = "&localization=false"
    
    # coins = ["bitcoin", "ethereum", "tether"]
    
    # dt = datetime(2022, 11, 29)
    
    key1 = "market_data"
    
    key2 = "current_price"
    
    key3 = "usd"
    
    
    for coin in coins:
        file = open("/home/ubuntu/environment/Week14/" + coin + ".csv", "w")
        dt = datetime(2022, 11, 29)
        for i in range(3):
            dt += timedelta(days=1)
            dts = dt.strftime("%d-%m-%Y")
            # print(url1 + coin + url2 + dts + url3)
            url =url1 + coin + url2 + dts + url3
            request = requests.get(url)
            time.sleep(6)
            request_dictionary = json.loads(request.text)
            
            file.write(dts + ", " + str(request_dictionary[key1][key2][key3]) + "\n")
            
        file.close()
            # next step
            # put info into a list
            # write lines into csv

def append_data(coins):
    coins = ["bitcoin", "ethereum", "tether"]
    
    url1 = "https://api.coingecko.com/api/v3/coins/"
    url2 = "/history?date="
    url3 = "&localization=false"
    # goes to stock market API and grab APPLE data, the adds it to a csv file
    # problem with te date is that its in newest to oldest data, so we have to reverse the data
    
    for coin in coins:
        dt = datetime(2022, 11, 29)
        dt += timedelta(days=1)
        dts = dt.strftime("%d-%m-%Y")
        url = url1 + coin + url2 + dts + url3
    
        print(url)
        req = requests.get(url)
        
        req_dict = json.loads(req.text)
        
        print(req_dict.keys())
        
        key1 = "Time Series (Daily)"
        key2 = '4. close'
        
        csv_file = open(coin + ".csv", "r")
        
        # pulling out data for comaoring purposes
        lines = csv_file.readlines()
        last_date = lines[-1].split(",")[0] # last element on the list, parced for the price
        
        
        new_lines = []
        
        for date in req_dict[key1]:
            if date == last_date:
                break
            
            print(date + "," + req_dict[key1][date][key2]) # print key and value
            # csv_file.write(date + "," + req_dict[key1][date][key2]+"\n")
            new_lines.append(date + "," + req_dict[key1][date][key2]+"\n")
            
        
        new_lines.reverse()
        csv_file = open(coin + ".csv", "a")
        csv_file.writelines(new_lines)
        csv_file.close()

def MeanReversionStrategy(prices, coin):
    print("\n" + coin + " Mean Reversion Strategy")
    # tells me what ticker I am running my function on
    i               = 0     # iterator set
    buy             = 0     # buy set
    total_profit    = 0     # total_profit set
    
    profit_list     = []    # list storage
    buys            = []
    sells           = []
    
    for price in prices:
        if i >= 5: # rolling average of 5 days
            current_price = price #the next price in the list
            average = (prices[i-1] + prices[i-2]+ prices[i-3] + prices[i-4] + prices[i-5]) / 5 #average price for the 5 previous days
            
            if current_price < average * 0.96 and buy == 0:
                # buy set to 0 so I only have 1 buy per loop
                buy = current_price
                print("buying at:", buy)
                buys.append(buy)
                # adding buy to list
                
            elif current_price > average * 1.04 and buy != 0:
                sell = current_price
                print("selling at:", sell)
                sells.append(sell)
                # adding sell to lsit
                profit = round(sell - buy, 2)
                # calculating profit
                profit_list.append(profit)
                print("trade profit:", profit)
                total_profit = total_profit + profit
                # calculating total profit from a base of 0
                buy = 0
                # setting buy back to 0
                
            else:
                pass # doesn't do anything
            
        i += 1 # entering iterator
        
    profit = sum(sells) - sum(buys)
    returns = (profit / sum(buys)) * 100
    
    print("_________________________")
    print("Total profit:", round(total_profit, 2))
    # rounded total profit
    print("First Buy:", buys[0])
    # first index of the buy list
    final_profit_percentage = (total_profit / buys[0]) * 100
    # calculating % return
    print("% Return", round(final_profit_percentage, 2), "%")
    print()
    
    return profit, returns
    # set my return call 
    
def SimpleMovingAverageStrategy(prices, coin):
    print("\n" + coin +  " Simple Moving Average Strategy")
    buys            = []    # lists and set zeros
    sells           = []
    buy             = 0
    sell            = 0
    i               = 0
    profit_list     = []
    total_profit    = 0
    
    for price in prices:
        if i >= 5: # rolling average of 5 days
            current_price = price
            average = (prices[i-1] + prices[i-2]+ prices[i-3] + prices[i-4] + prices[i-5]) / 5 
            #average price for the 5 previous days
            if current_price > average and buy == 0:
                buy = current_price
                print("Buying at:", buy)
                buys.append(buy)
                # adding it to list
                
            elif current_price < average and buy != 0:
                sell = current_price
                print("Selling at:", sell)
                sells.append(sell)
                # adding my sells to the list
                profit = round(sell - buy, 2)
                print("Trade Profit: ", profit)
                # calculating profit
                profit_list.append(profit)
                # tracking profits
                total_profit = total_profit + profit
                # again calculating total profit from a base of 0
                buy = 0 # setting buy back to 0
                
            else:
                pass
            
        i += 1 # iterator
        profit = sum(sells) - sum(buys)
        if sum(buys) == 0:
            pass
        else:
            returns = (total_profit / sum(buys)) * 100
            
    print("_______________________")
    print("Total Profit", round(total_profit, 2))
    # rounded total profit
    print("First Buy:", buys[0])
    # first buy from saved list
    final_profit_percentage = (total_profit / buys[0]) * 100
    print("% Return", round(final_profit_percentage, 2), "%")
    print()
    
    return profit, returns

# pull csvs into my code
# convert data into a prices list
# run data throguh the strategies
# Save results to a results file
# append data
# look into pulling the current date 
# change date format in csv files
def SaveResults(results):
    with open("results.json", "w") as f:
        json.dump(results, f)
        
results = {}

coins = ["bitcoin", "ethereum", "tether"]

for coin in coins:
    with open(f"./Week14/{coin}.txt", "r") as f:
        lines = f.readlines()
        prices = [float(line.strip()) for line in lines]
    
    initial_data_pull(coins)
    append_data(coins)
    
    
    results[f"{coin}_prices"] = prices
    
    mr_profit, mr_returns = MeanReversionStrategy(prices, coin)
    results[f"{coin}_mr_profit"] = mr_profit
    results[f"{coin}_mr_returns"] = mr_returns
    sma_profit, sma_returns = SimpleMovingAverageStrategy(prices, coin)
    results[f"{coin}_sma_profit"] = sma_profit
    results[f"{coin}_sma_returns"] = sma_returns
    
SaveResults(results)



def reading_the_data(coins):
    for coin in coins:
        file = open("/home/ubuntu/environment/Week14/" + coin + ".csv", "r")
    
        prices = [line for line in round(float(file.readlines().split(",")[1]),2)]
        
        print(prices)












# request = requests.get(url)
# request_dictionary = json.loads(request.text)

# print(request_dictionary["market_data"]["current_price"]["usd"])

# market_data

# "current_price"

# "usd"

