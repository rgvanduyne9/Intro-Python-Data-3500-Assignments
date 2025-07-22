# # sentinel value is used to break out of a loop, watches the while loop to see when we should end it
# response = input("Are you enjoying class?\n")

# while response == "yes":
#     print("That's awesome")
    
#     response = input("Are you still enjoying class?\n")
    
# # password check
# password_correct = False

# while password_correct == False:
#     password_input = input("Please enter password: ")
    
#     if password_input == "Password123":
#         password_correct = True
        
# sentinel and nested statements
# nested just means a chunk of code within another chunk of code; i.e. if statemet inside an if statement or in a while loop
# selection = 0

# while selection != 5:
#     print("Character choices:")
#     print("1. Mario")
#     print("2. Luigi")
#     print("3. Yoshi")
#     print("4. Peach")
#     print("Select 5 to quit")
#     selection = int(input("Please select a character (1-5):\n"))
#     if selection == 1:
#         print("It's a me! aMario!")
#     elif selection == 2:
#         print("Luigi time")
#     elif selection == 3:
#         print("Yoshi!!!")
#     elif selection == 4:
#         print("Yeah!")
#     elif selection == 5:
#         print("Thanks for playing!")
#     else:
#         print("Please select one of the main 5 choices.")

# for loop nested statement

for i in range(10):
    print("i:",i)
    
print()
    
for j in range(2,22,2):
    print("j:", j)
    
print()
    
for i in range(6):
    for j in range(6):
        print("i:", i, "j:", j)
        
print()
    
for i in range(6):
    for j in range(6):
        print("i*j:", i * j)
        
print()
    
for i in range(6):
    for j in range(6):
        print(i * j, end=" ")
        
print()
    
for i in range(6):
    print(end=" ")
    print()
    for j in range(1,6):
        print(i * j, end=" ")