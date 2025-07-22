def sum_all_values(lst):
    tot = 0
    for l in lst:
        tot += l
    return tot

# call function
list_fun = [1,2,3,4,5]
total = sum_all_values(list_fun)
print("total:", total)


def changeint(x):
    x = 9999999999
    return

def changelist(lst):
    lst[0] = 9999999999
    return

values = 10
changeint(values)
print("value:", values)

lst = [1,2,3,4,5]
changelist(lst)
print("list:",lst)

# this is because of mutable and immutable, mutable means changeable, immutable means not changeale
# lists are mutable, and integers are immutable