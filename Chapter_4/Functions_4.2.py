# there are built in functions for python
# a function is an integreated code that is embedded, or a chunk or logic that will do something for you every time

# old way
res1 = 2 ** 2
res2 = 3 ** 2
res3 = 4 ** 2
print(res1, res2, res3)

#function definition
def square(arg1, arg2):
    num = arg1 ** arg2
    return num
    
# function call
res1 = square(2,2)
res2 = square(3,2)
res3 = square(4,2)

print(res1, res2, res3)

# def means definition
# arg represents the numbers we want to sqr
# return ends the function

for i in range(1,101):
    print(square(i,2))
    
