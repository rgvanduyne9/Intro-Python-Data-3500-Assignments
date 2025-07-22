print("Rachel is an awesome coder")

# if else
status = "Struggling"
if status == "Struggling":
    print("Ask for help, and you will get help!")
else:
    print("Glad you are doing well!")
    
# else statement only runs if the first statement doesn't

# if elif else
num_grade = 75
if num_grade >= 90:
    print("You got an A!")
elif num_grade >= 80:
    print("You got a B")
elif num_grade >= 70:
    print("You got a C")
elif num_grade >= 60:
    print("You got a D")
else:
    print("You got an F:(")
#elif will only execute one of the statements

# multiple of statements
bozo_bucket = eval(input("What is the highest bucket you got to? "))
if bozo_bucket >= 1:
    print("You win a candy bar")
if bozo_bucket >= 2:
    print("You win a card game")
if bozo_bucket >= 3:
    print("You win a toy doll")
if bozo_bucket >= 4:
    print("You win a kite")
if bozo_bucket >= 5:
    print("You win a bicycle")
if bozo_bucket >= 6:
    print("You winn $100!")
else:
    print("Sorry you don't get anything:(")