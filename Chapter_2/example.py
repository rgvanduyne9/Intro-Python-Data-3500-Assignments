age = 25
typecar = "Honda Accord"
monday = True
# Monday is a boolian functin
# varaible names are case sensitive, M vs. m
print("monday: ", monday)

_1st_day_of_the_week = "Monday"
# if you want a variable to start with a # there must be and _ before it
_str = "This is a string!!"
# = is also called the assignment operator, us it to assign values

#Arithmetic in Python
age = 29 + 10
print("age: ", age)

#subtracction
age = age - 1
print ("age: ", age)

#multiplication
x = 3 * 2
print("x: ", x)

#division
x = 5 / 2
print("x: ", x)

# regular division vs. floor division
# floor division - decimals cut off

x = 5 // 2
print("x: ", x)

#modulus operator - returns remainder
x = 5 % 2
print("x: ", x)

# python will print out code line by line
# so if you just want to run a single code block you will need to commen everything else out
# to comment out a lot of code, crtl a --> ctrl /

# Exception, cant divide by 0
# order of operations, remember PEMDAS

print ("_str: ", _str)
print()
print("typecar: ", typecar)

# using print() give and empty space or blank line
# or you can use \n
# so:
 
print("_str: ", _str, "\n")
print("typecar: ", typecar)

# \t on test, what does it do? indents?
print()
print("\t", "typecar:", typecar)

pizza = """I'm going to talk about how much I love hawaiin. Yum. 
Pep. The best. wow.
Margarita pizza. Obvisouly the best one."""

print("pizza:", pizza)
# """ a triple indent will print your text out the same way you typed it in

'''
This is good for things that you don't want to print to the console, but you need to explain anyways.
'''

# ''' multi line comment