import json

def MeanReversionStrategy(prices):
    print(ticker, "Mean Reversion Strategy")
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
                print("buy at:", buy)
                buys.append(buy)
                # adding buy to list
                
            elif current_price > average * 1.04 and buy != 0:
                sell = current_price
                print("sell at:", sell)
                sells.append(sell)
                # adding sell to lsit
                profit = round(sell - buy, 2)
                # calculating profit
                profit_list.append(profit)
                print("profit:", profit)
                total_profit = total_profit + profit
                # calculating total profit from a base of 0
                buy = 0
                # setting buy back to 0
                
            else:
                pass
            
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
    


def SimpleMovingAverageStrategy(prices):
    print(ticker, "Simple Moving Average Strategy")
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
                print("Buy at:", buy)
                buys.append(buy)
                # adding it to list
                
            elif current_price < average and buy != 0:
                sell = current_price
                print("Sell at:", sell)
                sells.append(sell)
                # adding my sells to the list
                profit = round(sell - buy, 2)
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
    
def SaveResults(results):
    with open("hw5_results.json", "w") as f:
        json.dump(results, f, indent=4)
        
tickers = ["AAPL", "GOOG", "ADBE", "AMZN", "BA", "CMCSA", "CSCO", "CVX", "JPM", "V"]

results = {}

for ticker in tickers:
    with open(f"./HW5/{ticker}.txt", "r") as f:
        lines = f.readlines()
        prices = [float(line.strip()) for line in lines]
        
    results[f"{ticker}_prices"] = prices
    mr_profit, mr_returns = MeanReversionStrategy(prices)
    results[f"{ticker}_mr_profit"] = mr_profit
    results[f"{ticker}_mr_returns"] = mr_returns
    sma_profit, sma_returns = SimpleMovingAverageStrategy(prices)
    results[f"{ticker}_sma_profit"] = sma_profit
    results[f"{ticker}_sma_returns"] = sma_returns
    
SaveResults(results)