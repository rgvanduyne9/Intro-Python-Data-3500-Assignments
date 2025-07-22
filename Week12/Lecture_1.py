# import json

# #JSON - Java script object notation
# # url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=NG9C9EPVYBMQT0C8"


# # print("price:", json)

# harding_car = {}
# harding_car["make"] = "honda"
# harding_car["model"] = "accord"
# harding_car["year"] = "1993"
# harding_car["lock_type"] = "manual"
# harding_car["transmission_type"] = "manual"

# # print(harding_car["transmission_type"])

# # for key in harding_car.keys():
# #     print("key:", key, end=' ')
# #     print("value:", harding_car[key])

# # on hw 5, you need to take json results and save it to a json file

# # with open
# with open("/home/ubuntu/environment/Week12/text_example.txt", "w") as file:
# # w - write mode which creates a new file or if it does it will wipe it clean and rewrite stuff, a - append mode
#     new_sentence = "This si a really important message"
#     file.write(new_sentence)


# # we will put our hw path to hw 5 in here
# # this saves it to home directory
# with open("/home/ubuntu/environment/car.json", "w") as car_file:
#     json.dump(harding_car, car_file)
    
# # in hw 5 we should have a results.json file

# #in hw 5 we need a function called save results:
# #saveresults, should be simple and look liek this
# # results is a dictornary

# def saveResults(results): # results is a Python dictionary
#     #should dump results into a json file
#     # could add a line: file = open("/home/ubuntu...", "w")
#     # json.dump(results, file)
#     json.dump(results, open("/home/ubuntu/environment/HW5/results.json", "w"))
#     file.close()
#     return

# # will need to use write mode

# try, except

num1 = 2
num2 = 0

try:
    print(num1 / num2)
    # would bring an error
except:
    print("you cannot divide by 0")
    
print("Python still rocks steady though")
print("Here's some more math: 2/3=", 2/3)

try:
    with open("/home/ubuntu/environment/404_no_file.txt", "r"):
        print(file.readlines())

except:
    print("that file does not exist")