# Get all students and scores
students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name,score])

# Find the second lowest score
scores = []
for student in students:
    scores.append(student[1])
second_lowest_score = sorted(set(scores))[1]

second_lowest_students = [] 
for student in students:
    if second_lowest_score == student[1]:
        second_lowest_students.append(student[0])

for name in sorted(second_lowest_students):
    print name
