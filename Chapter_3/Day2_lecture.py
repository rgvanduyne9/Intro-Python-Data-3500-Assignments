# career expo this weekend
# ASC student showcase: Oct. 2yth at 12:30-2:30pm
# entreprenuership pitch Sept. 27th 6:30-8, contact Russell Fisher


# print all odd numbers 1 to 99


# print all odd numbers 1 to 99


# sum numbers 


# random
for i in range(1,8):
    print(i)
print()
# iderator, counts how may times you-ve ran the code, comouters count from 0 

for i in range(10):
    print(i)
print()

seasons = ["Summer", "winter", "second winter", "one week of spring"]

for season in seasons:
    print("seasons:", season)
print()

fav_season = "summer"

for letter in fav_season:
    print(letter)
print()

# augmented assignment
age = 36
age = age + 6
print("age:", age)
print()

age += 6
print("age:", age)

age -= 8
print("age:", age)

age /= 5
print("age:", age)

age *= 5
print("age:", age)
print()

for i in range(20):
    age += 1
    print("age:", age)
print()
    
counter = 0
for i in range(100):
    i *= i # TODO write code...
    counter += 1
    print("The value of i is:", i, "on iteration,", counter)

# print all odd numbers 1 to 99
for i in range(1,100):
    if i % 2 == 1:
        print(i,"is an odd number")
print()        
# print all odd numbers 1 to 99, step by
for i in range(1,100,2):
    print(i)
# step by (2) means every other

