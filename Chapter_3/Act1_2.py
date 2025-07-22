# 1
birth_year = eval(input("What year were you born?\n"))

if birth_year >= 1997:
    print("You belong to the Zoomer generation.")
elif birth_year >= 1981:
    print("You belong to the Millenial generation.")
elif birth_year >= 1965:
    print("You belong to Generation X.")
elif birth_year >= 1946:
    print("You are a Boomer.")
else:
    print("You're super old idk even know what generation that is.")

# 2
age = eval(input("How old are you?\n"))
current_year = 2023

while age > 0:
    print("You were alive in the current year", current_year)
    current_year -= 1
    age -= 1
else:
    print("You were born in the year", current_year)