age = eval(input("How old are you?\n"))
print()
print("You are", age, "years old.")
print()
desiredage = eval(input("What age would you like to live to?\n"))

yearsleft = desiredage - age

print("If you want to live to", desiredage, "and you are", age, "year(s) old,\nThat means, you have", yearsleft, "years left to live.")
print()

score = eval(input("What did you score in class?(As a %)\n"))
print("Score: %",score)
print()

if score >= 93:
    print("Congratualtions! You got an A!")
else:
    print("That's okay you still learned a lot!")
    