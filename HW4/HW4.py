# load stock prices
file = open("/home/ubuntu/environment/HW4/AAPL.txt")
# file opening is case sensitive

lines = file.readlines()
# readlines function goes through out file and reads the lines and feeds them back into our variable we are saving them to
 
prices = []


for line in lines:

    price = float(line)

    price = round(price, 2) # to round the price to 2 decimals

    prices.append(price)

# print(prices)

# run mean reversion strategy (5 day moving average)
i               = 0
buy             = 0
total_profit    = 0
profit_list = [] #tracking profit prices
buys = [] #tracking buying prices

for price in prices:
    if i >= 5: # rolling average of 5 days
        current_price = price #the next price in the list
        average = (prices[i-1] + prices[i-2]+ prices[i-3] + prices[i-4] + prices[i-5]) / 5 #average price for the 5 previous days
            
        # print("i: ", i,",", average)
            
        if current_price < average * 0.96 and buy == 0: # .96 if you use 2022 data
            # but set to == 0 so we only get 1 buy per loop
            buy = current_price
            print("buy at:", buy)
            buys.append(buy) #adding to list
        
        
        elif current_price > average * 1.04 and buy != 0: # 1.04 if you use 2022 data
            sell = current_price
            print("sell at:", sell)
            profit = round(sell - buy, 2) # calculate profit with 2 decimal places
            profit_list.append(profit) # tracking profits
            print("profit:", profit)
            total_profit = total_profit + profit #calculating total profit from the base 0 I set it to
            buy = 0 #setting buy back to 0 to go through the loop again
                
            
        else: 
            pass
            
    i += 1 #iterater

print("-------------------")
print("Total Profit:", round(total_profit, 2)) 
# rounded total profit
print("First Buy:", buys[0])
# first buy from the list i kept
final_profit_percentage = ( total_profit / buys[0] ) * 100
# % return using my tracked total profit and my first buy
print("% return:", round(final_profit_percentage, 2), "%")

# print output


# calculate final output and returns