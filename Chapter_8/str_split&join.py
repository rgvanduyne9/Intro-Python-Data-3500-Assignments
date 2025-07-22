# split
data_str = "1, 2, 3, 4, 5, 6"
lst = data_str.split(",")
print("lst:", lst)

#join
new_str = ",".join(lst)
print("new string:", new_str)

# join with list comprehension
str_lst = "-".join([str(i) for i in range(1, 101)])
print("str_lst:", str_lst)