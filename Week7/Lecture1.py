# fav_colors = ["Aggie Blue", "Fighting White", "Pink"]
# second_fav_colors = []
# print(fav_colors)
# print(second_fav_colors)
# # good practice to make the list name plural

# flowers = ["Sunflower", 67, True]
# # example of heterogeneous data

# fav_flowers = ["Sunflowers", "Rose"]
# prices = [45, 38, 2, 7, 9]
# # lists are mutable or changeable

# # append or insert, both add data to the list
# fav_colors.append("Green")
# print(fav_colors)

# fav_colors.insert(0, "Navy")
# print(fav_colors)
# print(fav_colors[1])

# print()

# print("My favorite colors:")
# for color in fav_colors:
#     print(color)

# print()    
# print(fav_colors.index("Pink"))

# # multiple instances of Pink
# # grabs first instance
# fav_colors2 = ["Pink", "Aggie Blue", "Fighting White", "Pink"]
# print(fav_colors2.index("Pink"))

# # number of items in the list
# # returns actual number not counting from 0
# print("My list of favorite colors is", len(fav_colors), "items long.")

# # remove & pop functions
# # pop takes last item on the list and throws it away, it's gone (specific spot)
# print("fav_colors: ", fav_colors)
# fav_colors.pop(3)
# print("fav_colors: ", fav_colors)

# # remove can be used for strings but pop cant (specific name)
# fav_colors.remove("Navy")
# print("fav_colors: ", fav_colors)

import random
# separate library we are pulling from

lst = []

for i in range(100):
    # name library before you use a function from it
    # randint is inclusive, so it will include 100
    lst.append(random.randint(1, 100))

print("Here's my random list: ", lst)