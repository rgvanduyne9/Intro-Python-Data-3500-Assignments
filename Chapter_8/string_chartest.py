# for isdigit and isalnum every character must be a digit or alpha numeric
# for the function to return true

# is digit
string = "12341234"
print(string.isdigit())

string = "-12341234"
print(string.isdigit())
# will return false becuase hyphen is not a digit, it check every character

# isalnum
address = "123 Main St"
print(address.isalnum())
# false, because it has spaces

address = "123MainSt"
print(address.isalnum())

address = "123 Main St. Logan, Utah"
print(address.isalnum())

address = address.replace(",", "")
address = address.replace(".", "")
address = address.replace(" ", "")

print(address)
print(address.isalnum())