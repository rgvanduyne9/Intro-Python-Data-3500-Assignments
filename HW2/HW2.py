# 2.3
grade = 91
if grade >= 90:
    print("Congratulations! Your grade of", grade, "earns you an A in this course.")
print()

# 2.4
x = 27.5 + 2
print(x)

x = 27.5 - 2
print (x)

x = 27.5 * 2
print(x)

x = 27.5 / 2
print(x)

x = 27.5 // 2
print(x)

x = 27.5 ** 2
print(x)

print()

#2.5
#circle
r = 2
pie = 3.14159

diameter = r * 2
print("Diameter:", diameter)

circumference = 2 * pie * r
print("Circumference:", circumference)

area = pie * (r ** 2)
print("Area of circle:", area)

print()

#2.6
num = eval(input("Input a number:\n"))

x = num % 2

if x == 0:
    print("Your number is even!")

if x == 1:
    print("Your number is odd!")
    
print()

#2.7
x = 1024

y = x % 4

if y == 0:
    print("Yes, 1024 is a multiple of 4!")
if y != 0:
    print("Whoops! It doesn't look like 1024 is a multiple of 4:(")
    
a = 2
b = 2 % 10

if b == 0:
    print("Yay 2 is a multiple of 10!! I don't know how that would be true though.")
    
if b != 0:
    print("2 is not a multiple of 10")
print()

#2.8
num_list = [0, 1, 2, 3, 4, 5]

print("Number\t\t Squared\t Cube")
for n in num_list:
    y = n ** 2
    x = n ** 3
    print(n,"\t\t", y,"\t\t",x)