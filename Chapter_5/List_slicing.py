# slicing operator

scores = [45, 39, 50, 49, 44]

for i in range(1, 5):
    print(scores[i])
    
scores_sliced = scores[1:5]
print(scores_sliced)

print(scores[:4])

print(scores[2:])