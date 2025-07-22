# Numpy Arrays
import numpy

# create a list of 4 floats
homework_scores = [49.5, 48.3, 47.6, 50]
print(homework_scores)

# conver the list into a numpy array
hw_np = numpy.array(homework_scores)
print(hw_np)

# Numpy array intitialization

# initialize a numpy array of size 10

np1 = numpy.zeros(100)
print(np1)

np2 = numpy.ones(100)
print(np2)

# Numpy array speed test
import numpy 
import random
import time

start = time.time()
randoms = []
for i in range(1000):
    randoms.append(random.randint(1,50))
end = time.time()
print(randoms)
print("time lapsed: ", end - start)

start2 = time.time()
rands = numpy.random.randint(50, size=1000)
end2 = time.time()
print(rands)
print("time lapsed: ", end2 - start2)