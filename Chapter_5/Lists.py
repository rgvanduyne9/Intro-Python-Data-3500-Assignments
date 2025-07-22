# homogeneous data - when a list stores the same type of data
# hetero geneous data, different types of data, like a row in a table
class_ages = [25, 54, 21, 22, 23, 24, 20, 19]
print()

print(class_ages)
print()
# computers count from 0
print(class_ages[3])
print(class_ages[2])
print(class_ages[1])
print(class_ages[0])
print()

for age in class_ages:
    print("age:", age)
print()
    
favorite_colors = ['aggie blue', 'fighting white', 'navy', 'red']
# nested for loop
for color in favorite_colors:
    print("color: ", color)
    for letter in color:
        print("letter: ", letter)

print()

name = "Rachel VanDuyne"

for letter in name:
    print(letter)

print()
print(name[0])
print(name[-1])
print(name[8])
print()

class_ages = [25, 54, 21, 22, 23, 24, 20, 19]

total = 0
count = 0

for age in class_ages:
    total += age
    count += 1
    
average = total / count
print("total:", total)
print("count:", count)
print("average:", average)


print("average: ", sum(class_ages) / len(class_ages))
print()
# part 2

# moving average (or rolling average. Like average of 3 then and average of the next three overlapping on spot 2)
prices = [140.1, 147.5, 145.25, 144.5, 145.5]
print("prices average:", sum(prices) / len(prices))

three_day_average = (prices[0] + prices[1] + prices[2])/3
print("3 day avg: ", three_day_average)

three_day_average = (prices[1] + prices[2] + prices[3])/3
print("3 day avg: ", three_day_average)

three_day_average = (prices[2] + prices[3] + prices[4])/3
print("3 day avg: ", three_day_average)

# My work
Movies = ['Percy Jackson and the sea of monsters', 'Harry Potter and the Half-Blood prince', 'About time', 'The perks of being a wallflower', 'The Iron Gaint']

for movie in Movies:
    print(movie)
 
print()
    
for i in range(len(Movies)):
    print(Movies[i])