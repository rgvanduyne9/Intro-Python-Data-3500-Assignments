#3.4
print("Problem 3.4:\n")

# Setting the number of rows I want displayed
for row in range (2):
# Setting the number of columsn I want displayed
    for col in range (7):
# Assigning what I want to be printed in each slot, and 
# making sure to include appropriate spacing
        print('@', ' ', end = '')
# The print statement below allows for the second row to be below the first
    print()

print()

# 3.9
print("Problem 3.9:\n")

x = True
# set a marker or sentinel value

while x == True:
    # use that value to control my whole loop
    n = (input("Please enter a 7 to 10 digit number: "))
    
    if len(n) < 7:
        print("You need at least 7 digits for this function.")
        # I use the len function to know how many variations of modulus operators and
        # floor division I should be using
        
    elif len(n) < 8:
        y = int(n)
        # in each of these n needs to go back to an integer to use it in math
        # modulus operator and floor division together get the individual digit alon
        d = y % 10000000 // 1000000
        e = y % 1000000 // 100000
        f = y % 100000 // 10000
        g = y % 10000 // 1000
        h = y % 1000 // 100
        i = y % 100 // 10
        j = y % 10 // 1
        print("\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n",i,"\n",j)
        break
    
    elif len(n) < 9:
        y = int(n)
        c = y % 100000000 // 10000000
        d = y % 10000000 // 1000000
        e = y % 1000000 // 100000
        f = y % 100000 // 10000
        g = y % 10000 // 1000
        h = y % 1000 // 100
        i = y % 100 // 10
        j = y % 10 // 1
        print("\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n",i,"\n",j)
        break
    
    elif len(n) < 10:
        y = int(n)
        b = y % 1000000000 // 100000000
        c = y % 100000000 // 10000000
        d = y % 10000000 // 1000000
        e = y % 1000000 // 100000
        f = y % 100000 // 10000
        g = y % 10000 // 1000
        h = y % 1000 // 100
        i = y % 100 // 10
        j = y % 10 // 1
        print("\n",b,"\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n",i,"\n",j)
        break
        
    elif len(n) < 11:
        y = int(n)
        a = y // 1000000000
        b = y % 1000000000 // 100000000
        c = y % 100000000 // 10000000
        d = y % 10000000 // 1000000
        e = y % 1000000 // 100000
        f = y % 100000 // 10000
        g = y % 10000 // 1000
        h = y % 1000 // 100
        i = y % 100 // 10
        j = y % 10 // 1
        print("\n",a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n",i,"\n",j)
        break
        
    else:
        x = True
        print("You cannot have more than 10 digits for this function.")

print()


# 3.11
print("Problem 3.11:\n")

miles_per_gallon = []
# stores inputs

x = True

# sentinel value to run my while loop

while x == True:
    
    user_input_gallons = float(input("Please enter gallons used or enter '0' to stop the program: "))
    # gather gallons input
    if user_input_gallons == 0:
        break
    
    user_input_miles = float(input("Please enter miles driven: "))
    # gather miles input
    mpg = user_input_miles / user_input_gallons
    # miles per gallon
    print("Miles/gallon for this tank: ", mpg)
    
    miles_per_gallon.append(mpg)
    # applies to variable into my list

print("Your average miles per gallon was: ", round(sum(miles_per_gallon) / len(miles_per_gallon),2))
# average miles per gallon
print()

# 3.12
print("Problem 3.12:\n")

number = int(input("Enter number:"))
    # gathering user input

sentinel = number 
    # using a sentinel value to track my input
reverse = 0
    # making default for the reverse 0
    
while(number > 0):
    
    last = number % 10
        # finding the last number found using modulus operator (like in class)
        
    reverse = reverse * 10 + last
        # middle number
    number = number // 10
        # first number

# letting the user know what they got
if(sentinel == reverse):
    print("Yay it's a plaindrome!")
    
else:
    print("Not a palindrome")

print()

last_problem = input("I put this here because otherwise python immediately goes to 3.14,\nenter anything to continue at it will spit out the iterations: ")
print()

# 3.14
print("Problem 3.14:\n")
# I see two iterations in a row of '3.14' begin at iteration 627 (so 627 and 628)
# I see two iterations in a row of 3.141 beginning at iteration 2454 (so 2454 and 2455)

numerator = 4
i = 1
pi = 0
total = 0 

for denominator in range(1, 6000, 2):
    if i % 2 == 0:
        total -= numerator/denominator
    else:
        total += numerator/denominator
    print("i:", i, "total:", total)
    i += 1
