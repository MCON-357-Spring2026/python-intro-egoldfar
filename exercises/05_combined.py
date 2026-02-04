"""
TODO:
Dictionary of students -> grades
Print averages
"""
students_grades = {"Alice": [98, 97, 95], "Bob": [86, 97, 90], "Charlie": [100, 98, 99], "David": [70, 75, 73]}

for student, grades in students_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student}: {average:.2f}")