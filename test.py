# Numbers = [1, 2, 3, 4, 5, 6, 7]

# Numbers2 = Numbers[4:7]

# print(Numbers2)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# rolling_averages = []

# for x in range(len(lst) - 2):
#     three_day_average = (lst[x] + lst[x+1] + lst[x+2]) / 3
#     rolling_averages.append(three_day_average)
    
# print(rolling_averages)
    
 

# favorite_colors = []

# for n in range(3):
#     colors = input("Please enter your favorite colors:\n")
#     favorite_colors.append(colors)

# print("here are your favorite colors:")
# for color in favorite_colors:
#     print(color)
    
    
for x in range(2, 21, 2):
    if x != 18:
        print(x, end=" ")
    else:
        end=" "
        
print()       
print("total: ", 9 ** (1/2))

for i in range(1, 6):
    print(i, i * 10, end=", ")