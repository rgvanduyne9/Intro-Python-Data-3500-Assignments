# open and write to file1
file1 = open("output1.txt", "w")
file1.write("hello\n")
file1.write("goodbye\n")
file1.close()

# open and write to file using "with"
with open("output2.txt", "w") as file2:
    file2.write("hello again\n")
    file2.write("goodbye again\n")
    
# reopen and read from file1
file1_again = open("output1.txt", "r")
print(file1_again.readlines())

# reopen and read from file2
file2_again = open("output2.txt", "r")
print(file2_again.readlines())