# #3.4

# # Setting the number of rows I want displayed
# for row in range (2):
# # Setting the number of columsn I want displayed
#     for col in range (7):
# # Assigning what I want to be printed in each slot, and 
# # making sure to include appropriate spacing
#         print('@', ' ', end = '')
# # The print statement below allows for the second row to be below the first
#     print()

# print()

# # 3.9

# # user_input = int(input("Please enter a 7 to 10 digit integer:\n"))

# # x = False

# # while x == False:
    
# # user_input = int(input("Enter a number between 7 and 10 digits long:\n"))
# user_input = 12345678

# i = 10000000000

# while i > 1:
#     if i > user_input:
#         print()
#     else:
#         print("User input is greater than i")
#         print(user_input // i)
#     i /= 10
    
# # user_input = 12345678

# # i = 10000000000

# # while i > 1:
# #     if i > user_input:
# #         print()
# #     else:
# #         print("User input is greater than i")
# #         print(user_input // i)
#     # i /= 10

# user_input = int(input("Please enter a 7 to 10 digit number:\n"))
# # x = False
# y = 10000000000

# # while x == False:
# #     print(user_input // y)
# #     x = True
    
# # 3.11
# # set up a sentinel value and while loops to add up values

# # 3.12
# number = 30303

# print("first: ", number // 10000)
# print("last: ", number % 10)

# # 3.14
# numerator = 4
# i = 1
# pi = 0
# total = 0 

# for denominator in range(1, 6000, 2):
#     if i % 2 == 0:
#         total -= numerator/denominator
#     else:
#         total += numerator/denominator
#     print("i:", i, "total:", total)
#     i += 1
# #iteration 627 AND 628 are where we see 3.14 twice




# number = int(input("Please enter a 7 to 10 digit number: "))

# while number > 0:
#     x = number % 10
#     print(x)
#     number = number // 10

# x = True

# while x == True:
#     n = (input("Please enter a 7 to 10 digit number: "))
    
#     if len(n) < 7:
#         print("You need at least 7 digits for this function.")
        
#     elif len(n) < 8:
#         y = int(n)
#         d = y % 10000000 // 1000000
#         e = y % 1000000 // 100000
#         f = y % 100000 // 10000
#         g = y % 10000 // 1000
#         h = y % 1000 // 100
#         i = y % 100 // 10
#         j = y % 10 // 1
#         print("\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n",i,"\n",j)
#         break
    
#     elif len(n) < 9:
#         y = int(n)
#         c = y % 100000000 // 10000000
#         d = y % 10000000 // 1000000
#         e = y % 1000000 // 100000
#         f = y % 100000 // 10000
#         g = y % 10000 // 1000
#         h = y % 1000 // 100
#         i = y % 100 // 10
#         j = y % 10 // 1
#         print("\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n",i,"\n",j)
#         break
    
#     elif len(n) < 10:
#         y = int(n)
#         b = y % 1000000000 // 100000000
#         c = y % 100000000 // 10000000
#         d = y % 10000000 // 1000000
#         e = y % 1000000 // 100000
#         f = y % 100000 // 10000
#         g = y % 10000 // 1000
#         h = y % 1000 // 100
#         i = y % 100 // 10
#         j = y % 10 // 1
#         print("\n",b,"\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n",i,"\n",j)
#         break
        
#     elif len(n) < 11:
#         y = int(n)
#         a = y // 1000000000
#         b = y % 1000000000 // 100000000
#         c = y % 100000000 // 10000000
#         d = y % 10000000 // 1000000
#         e = y % 1000000 // 100000
#         f = y % 100000 // 10000
#         g = y % 10000 // 1000
#         h = y % 1000 // 100
#         i = y % 100 // 10
#         j = y % 10 // 1
#         print("\n",a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n",i,"\n",j)
#         break
        
#     else:
#         x = True
#         print("You cannot have more than 10 digits for this function.")
    

    
# def getSum(n):
    
#     sum = 0
#     while (n != 0):
       
#         sum = sum + (n % 10)
#         n = n//10
       
#     return sum
   
# n = 569
# print(getSum(n))

# def printinteger(n):
    
#     integer = 0
#     while (n != 0):
        
#         integer = n % 10
#         n = n // 10
    
#     return integer

# n = int(input("Please enter a 7 to 10 digit number: "))
# print(printinteger(n),"\n")


# 3.11
# user_input = 0
# user_input_miles = 0
# stop_code = 1

# while stop_code != 0:
#     stop_code = float(input("Press 0 to stop or 1 to contiue: "))

#     if stop_code == 0:
#         break
        
#     else:
#         user_input += float(input("Please enter gallons used: "))
#         user_input_miles += float(input("Please enter miles driven: "))
#         print("Miles per gallon this tank: ", user_input / user_input_miles)
#         # miles_per_gallon = user_input / user_input_miles
    
#         # print("Miles per gallon for this tank: ", miles_per_gallon)
#         # print()
        
# print(f"Average miles per gallon: {user_input / user_input_miles}")

#array to store miles/gallon 
miles_gallon = []

#infinite loop to take inputs
while True:

  #if input is -1 break the loop
  gallon = float(input("Enter the gallons used(-1 to stop): "))

  if gallon == -1:
    break
  miles = float(input("Enter the miles: "))

  #calculate miles per gallon
  mg = miles/gallon
  print('miles/gallon for this tank : ',mg)
  miles_gallon.append(mg)

#calculate the overall average miles per gallon
print("The overall miles/gallon average :",sum(miles_gallon)/len(miles_gallon))