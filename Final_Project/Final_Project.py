import requests
import json
import time
from datetime import datetime, timedelta, date

# importing relevant codes


# url =  "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=29-11-2023&localization=false"

def initial_data_pull(coins):
    coins = ["bitcoin", "ethereum", "tether", "litecoin", "ripple", "eos"]
    # identify the coins we will use
    url1 = "https://api.coingecko.com/api/v3/coins/"
    url2 = "/history?date="
    url3 = "&localization=false"
    # url split into pieces to be able to iterae through the coins
    
    # identifying keys
    
    key1 = "market_data"
    
    key2 = "current_price"
    
    key3 = "usd"
    
    # for loop to pull data for each coin
    for coin in coins:
        file = open("/home/ubuntu/environment/Final_Project/Data/" + coin + ".csv", "w")
        dt = datetime(2022, 11, 29)
        # file path and beginning date set up
        
        for i in range(364):
            # 364 so we can do a whole year (0, 364)
            dt += timedelta(days=1)
            # adding one day in at a time from beg. date
            dts = dt.strftime("%d-%m-%Y")
            # standardizing date format
            url = url1 + coin + url2 + dts + url3
            # set up whole url to use for each coin
            request = requests.get(url)
            # using the url
            time.sleep(6)
            request_dictionary = json.loads(request.text)
            # loading in the data
            
            file.write(dts + "," + str(request_dictionary[key1][key2][key3]) + "\n")
            # writing the data
            
        file.close()
            # closing out file when the year is complete

def append_data(coins):
    coins = ["bitcoin", "ethereum", "tether", "litecoin", "ripple", "eos"]
    # list coins
    
    url1 = "https://api.coingecko.com/api/v3/coins/"
    url2 = "/history?date="
    url3 = "&localization=false"
    # define and assign url pieces
    
    key1 = "market_data"
    key2 = "current_price"
    key3 = "usd"
    # define keys from the url or api
    
    for coin in coins:

        file = open("/home/ubuntu/environment/Final_Project/Data/" + coin + ".csv", "r")
        # open in read mode
        # reading the lines
        lines = file.readlines()
        last_date = lines[-1].split(",")[0]
        # parcing out the date
        file.close()
        
        dt = date.today()
        dts = dt.strftime("%d-%m-%Y")
        # getting todays date for comparison
        
        url = url1 + coin + url2 + dts + url3
        # creating the url for the coin
        
        req = requests.get(url)
        req_dict = json.loads(req.text)
        # loading in the url and text
        
        
        new_lines = []
        # new lines list for data we need to append if at all
        
        while str(dts) > last_date:
            new_lines.append(dts + "," + str(req_dict[key1][key2][key3] + "\n"))
            # appending it to list and parcing through the data for correlating keys to do so
            dt_object = datetime.strptime(dts, "%d-%m-%Y")
            # standardizing format
            new_dt_object = dt_object-timedelta(days=1)
            # subtracting one day from the date
            new_dts = new_dt_object.strftime("%d-%m-%Y")
            # converting results back into string
            dts = new_dts
        csv_file = open("/home/ubuntu/environment/Final_Project/Data/" + coin + ".csv", "a")
        csv_file.writelines(new_lines)    
        csv_file.close
        # writing in the new lines if we have any to the csv and appending then closing it

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
                print("buying at:", round(buy, 2))
                buys.append(buy)
                # adding buy to list
                
            elif current_price > average * 1.04 and buy != 0:
                sell = current_price
                print("selling at:", round(sell, 2))
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
        
        
    # if else statements implemented to help the code run if or when there is no buy or sell
    # so that the code doesn't break
    profit = sum(sells) - sum(buys)
    if sum(buys) == 0:
        returns = "No returns"
    else:
        returns = (profit / sum(buys)) * 100
    
    print("_________________________")
    print("Total profit:", round(total_profit, 2))
    # rounded total profit
    if len(buys) == 0:
        print("No Buys or Final Profit Percentage")
    else:
        print("First Buy:", round(buys[0], 2))
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
                print("Buying at:", round(buy, 2))
                buys.append(buy)
                # adding it to list
                
            elif current_price < average and buy != 0:
                sell = current_price
                print("Selling at:", round(sell, 2))
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
        
    # if else statements implemented to help the code run if or when there is no buy or sell
    # so that the code doesn't brea
            
        i += 1 # iterator
        profit = sum(sells) - sum(buys)
        if sum(buys) == 0:
            returns = "No Returns"
        else:
            returns = (total_profit / sum(buys)) * 100
            
    print("_______________________")
    print("Total Profit", round(total_profit, 2))
    # rounded total profit
    if len(buys) == 0:
        print("No buys")
    else:
        print("First Buy:", round(buys[0], 2))
    # first buy from saved list
    if len(buys) == 0:
        print("No Final Profit Percentage")
    else:
        final_profit_percentage = (total_profit / buys[0]) * 100
        print("% Return", round(final_profit_percentage, 2), "%")
    print()
    
    return profit, returns

def SaveResults(results):
    with open(f"./Final_Project/results.json", "w") as f:
        json.dump(results, f)
        
    # dumping results into my json file
        
results = {}
# setting up results dictionary

coins = ["bitcoin", "ethereum", "tether", "litecoin", "ripple", "eos"]
# assigning the coins I want to analyze

initial_data_pull(coins)
append_data(coins)
# calling these functions outside the for loop because I only need to run them once before

for coin in coins:

    # opening my file path in read mode for analysis
    with open(f"./Final_Project/Data/{coin}.csv", "r") as f:
        lines = f.readlines()
        prices = [float(line.split(",")[1].strip()) for line in lines]
        # spliting and striping my csv's so I can run analysis on just the prices
    
    results[f"{coin}_prices"] = prices
    mr_profit, mr_returns = MeanReversionStrategy(prices, coin)
    results[f"{coin}_mr_profit"] = mr_profit
    results[f"{coin}_mr_returns"] = mr_returns
    sma_profit, sma_returns = SimpleMovingAverageStrategy(prices, coin)
    results[f"{coin}_sma_profit"] = sma_profit
    results[f"{coin}_sma_returns"] = sma_returns
    # calling the analsysis on just the prices, while stating what coin its running on
    
SaveResults(results)