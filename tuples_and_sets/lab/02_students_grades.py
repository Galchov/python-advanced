import sys
from io import StringIO

test_input_1 = """7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.00
"""
test_input_2 = """4
Scott 4.50
Ted 3.00
Scott 5.00
Ted 3.66
"""
test_input_3 = """5
Lee 6.00
Lee 5.50
Lee 6.00
Peter 4.40
Kenny 3.30
"""


# sys.stdin = StringIO(test_input_1)


def average(values):
    """Returns the average of the student's grades"""

    return sum(values) / len(values)


n = int(input())

students_record = {}

for _ in range(n):
    name, grade_string = input().split(' ')
    grade = float(grade_string)

    if name not in students_record:
        students_record[name] = []

    students_record[name].append(grade)

for name, grades in students_record.items():
    average_grade = average(grades)
    grades_string = ' '.join(str(f'{x:.2f}') for x in grades)
    print(f'{name} -> {grades_string} (avg: {average_grade:.2f})')
