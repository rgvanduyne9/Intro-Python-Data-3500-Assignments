#1
apple_price = 2.5
#2
number_purchased = 3
#3
tax = 1.07
#4
total_bill = apple_price * number_purchased * tax
#5 & 6
if total_bill == 0:
    print("Please recheck your inputs")
else:
    print("Apples purchased:", number_purchased)
    print("Total bill: $", round(total_bill,2))
