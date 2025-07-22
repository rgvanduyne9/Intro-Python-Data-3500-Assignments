# a list of lists

# 2d list
tab = []
for i in range (10):
    tab.append([])

for i in range(10):
    for j in range(10):
        tab[i].append( i * j)

print(tab, "\n")

for row in tab:
    print(row)
    
for i in range(10):
    for j in range(10):
        print(tab[i][j], end =" ")
    print()

# list of student scores
johnny = [49, 48, 50]
sally = [49, 50, 50]
jenny = [50, 50, 50]

student_scores = [johnny, sally, jenny]

for student in student_scores:
    print(student)
    
for student in student_scores:
    for score in student:
        print(score, end=" ")
    print()
    
for student in student_scores:
    for score in student:
        print(score, end=" ")
        print()