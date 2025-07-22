# if your code was going to break on something, you can ,ake code so that it will run over it
# makes it so you can keep running the rest of your code despite the error

# try except block

try:
    open("this file doesn't exist")
except:
    print("this file cannot be opened, doesn't exist")
 
try:
    print(0/5)
    print(5/0)
except:
    print("someone put a zero in the denominator")

print("the python code is still running")
