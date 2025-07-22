# Wednesday stuff

# numpy is a library in python; the array object that encapsulates n-dimensional heterogeneous data types
# allows for quicker run time

# import os
# os.system("sudi pip install numpy")

import numpy

numpy_zeros_array = numpy.zeros(30)
print(numpy_zeros_array)

prices = [125.45, 230.87, 982.00, 678.9, 312.98]
print("prices", prices)

np_prices = numpy.array(prices)
print(np_prices)

# could use it in your final project to make it run faster
# numpy is great or large sets of data (1000000)

print()

# strings

# capitalize()
# lower()
# upper()

# name_list= []

name = "Professor"
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name)

# for x in name:
#     print(x)
#     name_list.append
    
# print(name_list[0].upper, name_list[1].upper)
print()
print(name.istitle())
# check to see if name starts with a capital

print(name.isupper())
# checks to see if everything is capitalized

print()

def count_title_case(sentence):
    count = 0
    words = sentence.split()
    # splits on a space by default, could add " " or "" to do it yourself
    print(words)
    for word in words:
        if word.istitle():
            count+=1
        else:
            pass
    print("counter:", count)


sentence = "Python is a Really Amazing Coding language. I love IT"

count_title_case(sentence)

print()

# coding activities 3 & 4

# 3
x = input("Please enter your name:\n")
y = x.upper()
print("welcome,", y+"!")

# 4
word_list = []
sentence = "dude, I just biked down that mountain and at first I was like Whoa, and then I was like Whoa"
words = sentence.split()
for word in words:
    word_list.append(word)

    
word_list[0] = word_list[0].capitalize()
word_list[13] = word_list[13].lower()
word_list[19] = word_list[19].upper()
word_list.append("!")

my_sentence = ' '.join(map(str,word_list))
print(my_sentence)

# challenge question

# sentence = input("Please write a sentence:\n")

# def swap_case(sentence):
#     new_sentence = []
#     for x in sentence:
#         new_sentence.append(x)
#     for y in new_sentence:
#         if y == y.upper():
#             y = y.lower.append(y)
#         elif y == y.lower():
#           y =  y.upper.append(y)
#         else:
#             pass
#     string_sentence = ''.join(map(str,new_sentence))
#     print("New characters sentence:",string_sentence)
    
# swap_case(sentence)