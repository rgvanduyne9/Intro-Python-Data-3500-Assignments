# Opening a file in read mode
file = open("/home/ubuntu/environment/Chapter_9/example.txt", "r")

# Reading the entire contents of file
# content = file.read()
# print("content:", content)

# Reading the file line by line
lines = file.readlines()
for line in lines:
    print("line:", line)

# closing the file
file.close()

# Opening a file in write mode
file = open("output.txt", "w")

# writing data to the file
# file.write("Hello world!\n")
# file.write("This is a new line in my file!!!\n")

# closing the file
file.close()