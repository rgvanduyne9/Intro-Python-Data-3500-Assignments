# age = 25
# print("age:", age)
# print(type(age))
# age = float(age)
# print(type(age))
# print("age: ", age)

# age = str(age)
# print(type(age))
# print("age:", age)

# print()

# # if statements

# age = 2

# if age == 18:
#     print("Congrats, you're an adult.")
# if age < 18:
#     print("Congrats, you're almost an adult...")
# if age > 18:
#     print("Congrats, you're old.")
    
# print()
    
# grade = 86

# if grade >= 93:
#     print("You got an A!")
    
# if grade < 93:
#     print("You still have time to get an A.")
    
# print()
    
# day = input("What day of the week is it?\n")
# print("\nIt is: ", day, "which means it's going to be an awesome day!")

# hobby = input("what is you favorite hobby?\n")
# print("You like to ", hobby, "which is pretty neat!")

# height = float(input("How tall are you? \n"))
# print("You are", height, "inches tall)

# does my car need an emissions test?
caryear = eval(input("What year was you car made?\n"))
print()

currentyear = 2023 

if currentyear % 2 == 0:
    print("It is an even year!")
    
if currentyear % 2 != 0:
    # print("It is an odd year")
    
    if caryear % 2 != 0:
        print("You need an emissions test.")
    if caryear % 2 == 0:
        print("You do not need an emissions test.")
        
# could do if currentyear - caryear == 0:
    # print("You do not need and emission test.")
    
# else:
    # print("You need an emissions test.")