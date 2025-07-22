# appending data to data sets

import requests
import json


def append_data():
    ticker = 'AAPL'
    url = 'http://www.alphavantage.co.query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    # goes to stock market API and grab APPLE data, the adds it to a csv file
    # problem with te date is that its in newest to oldest data, so we have to reverse the data
    
    print(url)
    req = requests.get(url)
    
    req_dict = json.loads(req.text)
    
    print(req_dict.keys())
    
    key1 = "Time Series (Daily)"
    key2 = '4. close'
    
    csv_file = open(ticker + ".csv", "r")
    
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
    csv_file = open(ticker + ".csv", "a")
    csv_file.writelines(new_lines)
    csv_file.close()