# a boolean statement or whatever is true or false
# every if statement needs to have a colon: and everything included in it must be indented
if 5 > 10: # false
    print("5 is greater")
    # line of code
    # line of code
# this line is outside of my if statement
if 10 > 5: # true
    print("10 is greater")
    
print(10 < 5)
print(10 > 5)
print(10 <= 5)
print(10 >= 5)
# print(10 = 5) would error
print(10 == 5)
print(10 != 5)

age = 25
your_age = input("Enter your age: ")
your_age = eval(your_age)

if your_age < age:
    print("You are younger than Chelsea")
    
if your_age > age:
    print("You are older than Chelsea")