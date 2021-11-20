import sys
from io import StringIO


test_input_1 = """2
1, 2, 3
4, 5, 6
"""

test_input_2 = """3
10, 2, 21, 4
5, 20, 41, 9
6, 2, 4, 99
"""

# sys.stdin = StringIO(test_input_2)


def read_matrix():
    """Returns a matrix from the input integers, spit by ', '"""

    n = int(input())

    matrix = []

    for _ in range(n):
        row = []
        for x in input().split(', '):
            row.append(int(x))
        matrix.append(row)

    return matrix


matrix = read_matrix()
flattened_matrix = []

for row in matrix:
    for column in row:
        flattened_matrix.append(column)

print(flattened_matrix)
