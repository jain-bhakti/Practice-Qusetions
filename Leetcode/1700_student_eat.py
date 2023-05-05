from collections import Counter

students = [1,1,0,0]
sandwiches = [0,1,0,1]
mycounter = Counter(students)
for sandwich in sandwiches: 
    if mycounter[sandwich] == 0:
        break
    else:
        mycounter[sandwich] -= 1

print(mycounter.total())
