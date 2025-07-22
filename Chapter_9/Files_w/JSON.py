# good for interacting with cloud based servers
# almost identical to python dictionaries
# is an acronym (JSON)

import json

my_hobbies = {}
my_hobbies["outdoors"] = ["disc gold", "hike", "ski", "paddle board"]
my_hobbies["indoors"] = ["read", "write", "sew", "watch movies"]
my_hobbies["tv_shows"] = ["The crown", "The queen's gambit"]

print(my_hobbies)

# save it into a json object
json.dump(my_hobbies, open("my_hobbies.json", "w"))
# takes in 2 arguments, the dictionary you want to save, and a file name

d1 = json.load(open("my_hobbies.json", "r"))
print(d1)