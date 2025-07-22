# string.count() function

phrase = "to be or not to be that is the question"
# how many times a phrase in a strong occurs
ct = phrase.count("to")
print("ct:", ct)
#starts counting in index 1, so second letter since it counts from 0
ct = phrase.count("to", 1)
print("ct:", ct)

ct = phrase.count("to", 14)
print("ct:", ct)

# string.index() function

idx = phrase.index("to")
print("idx:", idx)
#starts it at index 10 count and doesn't include the first "to"
idx = phrase.index("to", 10)

# string.rindex() function
# starts counting from the right
idx = phrase.rindex("to")
print("idx:", idx)