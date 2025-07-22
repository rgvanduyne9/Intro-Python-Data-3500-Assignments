pi = input("Enter pi: ")
# input is a function that lets you creat a string that is user interactive
print(type(pi))
print ("pi: ", pi)

# anything the use inputs into your program will be fed bac as a string, you have to change this yourself

pi = eval(pi)
print(type(pi))
print ("pi: ", pi)