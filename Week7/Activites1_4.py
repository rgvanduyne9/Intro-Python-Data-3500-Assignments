# 1
colors = ["Blue", "Green", "Pink"]

print("My favorite colors:\n")
for color in colors:
    print(color)
    
print()

# 2
print("My favorite colors:\n")
for color in colors:
    print(color)
    for x in color:
        print(x)
print()
        
# 3
import random

my_list = []

for x in range(10):
    my_list.append(random.randint(1,10))
    
print("My List #1: ", my_list)

# 4
import random

my_list = []

for x in range(10):
    my_list.append(random.randint(1,10))
    
print("My List: ", my_list)

even_numbers = []

for i in my_list:
    even = i % 2
    even_numbers.append(even)
    # print(i, i+1)

print(even_numbers)



if even_numbers[0] == 0 and even_numbers[1] == 0:
    print("Spots 0 and 1 have even numbers:", even_numbers[0], even_numbers[1])
    

if even_numbers[1] == 0 and even_numbers[2] == 0:
    print("Spots 1 and 2 have even numbers:", even_numbers[1], even_numbers[2])
    

if even_numbers[2] == 0 and even_numbers[3] == 0:
    print("Spots 2 and 3 have even numbers:", even_numbers[2], even_numbers[3])
    

if even_numbers[3] == 0 and even_numbers[4] == 0:
    print("Spots 3 and 4 have even numbers:", even_numbers[3], even_numbers[4])
    

if even_numbers[4] == 0 and even_numbers[5] == 0:
    print("Spots 4 and 5 have even numbers:", even_numbers[4], even_numbers[5])
    

if even_numbers[5] == 0 and even_numbers[6] == 0:
    print("Spots 5 and 6 have even numbers:", even_numbers[5], even_numbers[6])
    

if even_numbers[6] == 0 and even_numbers[7] == 0:
    print("Spots 6 and 7 have even numbers:", even_numbers[6], even_numbers[7])
    

if even_numbers[7] == 0 and even_numbers[8] == 0:
    print("Spots 7 and 8 have even numbers:", even_numbers[7], even_numbers[8])
    

if even_numbers[8] == 0 and even_numbers[9] == 0:
    print("Spots 8 and 9 have even numbers:", even_numbers[8], even_numbers[9])
    
    