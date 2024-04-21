# write a program that converts students marks into grades
student_marks = {
    'Jenny': 92,
    'Harry': 78,
    'Dimpy': 56,
    'Rahul': 41,
    'Aniket': 99,
    'Prem': 34}
# The rating system is as follows : 90 - 100 (A+), 80 - 90 (A), 70 - 80 (A-)
# 60 - 70 (B), 50 - 60 (C), 40 - 50 (D) below 40 (F)
student_grades = {}
for i in student_marks:
    marks = student_marks[i]
    if 90 <= marks <= 100:
        student_grades[i] = 'A+'
    elif 80 <= marks <= 90:
        student_grades[i] = 'A'
    elif 70 <= marks <= 80:
        student_grades[i] = 'A-'
    elif 60 <= marks <= 70:
        student_grades[i] = 'B'
    elif 50 <= marks <= 60:
        student_grades[i] = 'C'
    elif 40 <= marks <= 50:
        student_grades[i] = 'D'
    else:
        student_grades[i] = 'F'
print(student_grades)
