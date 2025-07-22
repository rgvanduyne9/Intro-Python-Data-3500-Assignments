# final project start
# stock market trading

# read in api from stock, link in slack
# also in week 13, process json content video

import json
import requests

ticker = "AAPL"

url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
# meta data, data about data

request = requests.get(url)
# code 200 means everything is running smoothly

rqst_dictionary = json.loads(request.text)

# print(rqst_dictionary)
# print(rqst_dictionary.keys())

key1 = "Time Series (Daily)"

# I need ALL the dates

key2 =  "4. close"

# part 2
file = open("/home/ubuntu/environment/Final_Project/AAPL.csv", "w")
# open in W(rite) mode

# reversing list so the ascend from day 0

lines = []

# back to part 1
for date in rqst_dictionary[key1].keys():
    # print(date, rqst_dictionary[key1][date][key2])
    
    # its only printing the data and key2 (price) because time series daily
    # is essentially just a dictionary or list that is storing the date
    
    # part of part 2
    lines.append(date + ", " + rqst_dictionary[key1][date][key2] + "\n")
    # ^^ part of reversing lines


# reversing the lines still
lines = lines[::-1]

file.writelines(lines)

file.close()

# one problem we could encounter is prices descend instead of increase from day 0
# also the two data per line

# part 2 complete

# back to part 1   
# print(rqst_dictionary[key1].keys())

# part 1 of the final complete (obtaining data from a web JSON API)


# now appending new data to our data set
