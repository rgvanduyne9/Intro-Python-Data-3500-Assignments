# 4.9 - Function Defaults
# 4.3 - function arguments

# function definition
def biggest(arg1=0, arg2=0, arg3=0, arg4=0):
    num = max(arg1, arg2, arg3, arg4)
    return num
    
# for every function: it needs a name (defintion), it needs arguments (parameters),
# created the main code(body), and made the return statement

# function call
res1 = biggest(2,4,6,8)
print(res1)

res2 = biggest(-1, -2, -3, -4)
print(res2)

# defaults are default settings for the arguments
# so, if someone forgets to put in an argument it will use 0 as default

res3 = biggest()
print(res3)

# similar to how print() works

res4 = biggest(10)
print(res4)

res5 = biggest(-10, -5)
print(res5)

res6 = biggest(-10, -5, 100)
print(res6)

# default settings make your code more robust, it helps the code not break
# default settings make your code better to share, default settings are readable and allow others to know whether they can easilt use it or not too
