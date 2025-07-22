# Person 1 task
# def us_conversion:
#def foreign_conversion():
# def main()

# US_dollar = float(input("How many US dollars do you have?\n"))

# exchange_rate = float(input("What is the exchange rate for the country you are going to?\n"))

# task 1

def us_conversion(US_dollar=0, exchange_rate=1):
    new_currency = US_dollar / exchange_rate
    return new_currency

# task 2
def foreign_conversion(exchange_rate=1, foreign_currency=0):
    new2_currency =  foreign_currency * exchange_rate
    return new2_currency

# task 3
def main(Canada=1.25, Mexico=0.05355, Japan=0.00668, England=1.22, Australia=0.6329):
    return 

user_input = input("Would you like to convert to USD or a foreign currency?\n")
