# create a dictionary
person = {}
person["name"] = "Rachel"
person["age"] = 20
person["employer"] = "Utah State University"
person["height_inches"] = 65
person["favorite_movies"] = ["Marvel", "Jurassic Park", "Treasure Planet"]

# access individual elements of a dictionary
print(person["name"])
print(person["age"])

# access elements in a loop
for key in person.keys():
    print(key, ":", person[key])