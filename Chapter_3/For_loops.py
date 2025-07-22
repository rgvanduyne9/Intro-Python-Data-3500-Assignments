#for loops only run for a certain amount fo time
# for loop through a string
name = "Rachel VanDuyne"
for character in name:
    print("character: ", character)

# or

for n in name:
    print(n, end= "")

#for loop using a list
fav_colors = ["blue, green, pink"]
for color in fav_colors:
    print("color: ", color)

# for loop using range
for r in range(1, 11):
    print("r:", r)
# computers count from 0
# so 10 characters in 0-9

i = 1
while i < 11:
    print("i: ",i)
    i += 1