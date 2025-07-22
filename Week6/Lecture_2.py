# function definition
def biggest(arg1, arg2, arg3, arg4, arg5=0, arg6=0):
    num = max(arg1, arg2, arg3, arg4, arg5, arg6)
    return num
    
# function call
res1 = biggest(2,4,6,8)
print(res1)

res2 = biggest (-1,-2,-3,-4)
print(res2)

def hello_world(user_input="hello_world"):
    print(user_input)
    
hello_world("Today is a rainy day")
hello_world()
