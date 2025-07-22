# Activity 1
palindrome = int(input("Please enter a 3 digit number:\n"))

x = palindrome // 100

y = palindrome % 10

print()

if x == y:
    print("Congratulations, your number is a palindrome!!")
else:
    print("Aw, it doesn't look like your number is a palindrome :/")
    
# Activity 2
# y = (1/2) + (1/4) + (1/8) + (1/16) + (1/32)

# denominator = 0


# for n in range (2, 1000):
#   while denominator <= 1000:
#       x = y + y
#       print(denominator,":", x)
#       denominator +=1
#       y = x
# --wrong

# Activity 2
counter = 0
x = 1
y = 2

for n in range(2,1000):
    while counter <= 1000:
        z = x / y
        print(counter,":", z)
        counter += 1
        x = z
        
integerx = int(x)
integerz = int(z)
intergery = int(y)

sum(x)
print(sum(x))