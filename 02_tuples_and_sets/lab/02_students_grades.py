def average_grade(grades_list):
    return sum(grades_list) / len(grades_list)


count = int(input())

students = {}

for _ in range(count):
    data = tuple(input().split())
    student, grade = data
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grades in students.items():
    grades_str = ' '.join(f'{g:.2f}' for g in grades)
    avg_grade = average_grade(grades)
    print(f"{student} -> {grades_str} (avg: {avg_grade:.2f})")
