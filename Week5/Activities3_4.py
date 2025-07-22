# # continue - skip

# for i in range(1,11):
#     if i == 9:
#         continue
#     else:
#         print(i)
        
# print()

# # break - stop

# for i in range(1,11):
#     if i == 9:
#         break
#     else:
#         print(i)
        
# print()
        
# # w/ while loops

# age = 30
# while age >= 30:
#     print(age)
#     age += 1
#     if age == 52:
#         break
    
# print()

# # Booleans - True or False

# is_raining = False
# is_sunny = False

# if is_raining == False:
#     if is_sunny:
#         print("It's a great day for the beach!")
#     else:
#         print("It's a cloudy day, but have fun at the beach.")
# else:
#     print("It's raining, but you could still go the beach.")
    
# print()

# # Boolean functions - and, or, not

# # and

# act_score  = 25
# passed_math1050 = True

# if act_score >= 25 and passed_math1050:
#     print("You can take Calc 1, cool beans!")
# elif act_score >= 25 and passed_math1050 == False:
#     print("You need to take 1050 again.")
# else:
#     print("You need to take the Alek's placement test, gross.")
    
# print()

# # or

# age = 18
# citizen = True

# if age >= 18 or citizen:
#     print("You can vote!")
# else:
#     print("You can't vote.")
    
# print()

# # not

# door_open = True

# if not door_open:
#     print("The door is not open.")
# else:
#     print("The door is open.")
    
# print()

# # Activity 3:
# # Look at Activity 3 for boolean True/False variables to be used

# child_age = int(input("Please enter your child's age:\n"))
# print()
# child_weight = int(input("Please enter your child's weight in Ibs:\n"))

# if child_age >= 12:
#     print("(1) Your child can sit in the front seat.")
    
# elif child_age == 11 and child_weight > 90:
#     print("(2) Your child may sit in the front seat.")

# elif child_age < 11 and child_weight > 100:
#     print("(3) Your child may sit in the front seat.")

# else:
#     print("Your child may not sit in the front seat.")
    
# print()

# challenge question
print("To create the best password, please meet these criteria listed below:\n")
print(" - must contain at least 8 characters\n - must contain at least 1 capital letter\n - must contain at least 1 lowercase letter\n - must contain at least 1 digit.")

print()

Pass_input = input("Please enter a password:\n")
print()

# criteria password must meet

criteria_1 = len(Pass_input)
criteria_2 = sum(1 for x in Pass_input if x.isupper())
criteria_3 = sum(1 for y in Pass_input if y.islower())
criteria_4 = sum(1 for z in Pass_input if z.isdigit())
strong_pass = False

if criteria_1:
    strong_pass = True

if criteria_2:
    strong_pass = True
    
if criteria_3:
    strong_pass = True
    
if criteria_4:
    strong_pass = True

if criteria_1 and criteria_2 and criteria_3 and criteria_4:
    print("Strong Password.")
else:
    print("Check criteria again.")