# List Comprehensions

# Adding values to a list with a for loop
# EX: expression for item in iterable if condition

lst = []
for i in range(100):
    lst.append(i)

print("lst:", lst)
print()

# list comprehension
# shorter way to do the code above
lst2 = [i for i in range(50)]
print("lst2:", lst2)

#[expression for item in iterable if condition]

# updating each value in a list comprehension
print()
lst = [str(i) for i in range(25)]
print("lst:", lst)

# list comprehension example
file = open("/home/ubuntu/environment/HW4/AAPL.txt")
lines = file.readlines()

prices = []
for line in lines:
    prices.append(float(line))
    
print("prices:", prices)

# could do this instead for prices

prices = [float(line) for line in lines]