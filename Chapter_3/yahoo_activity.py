roku_prices = [73.17, 73.81, 74.39, 76.26, 77.80]
total = 0
length = 0
# the are just adj. prices for Roku
for price in roku_prices:
    total += price
    length += 1
    
avg = total/length
print("Average:", round(avg, 2))
