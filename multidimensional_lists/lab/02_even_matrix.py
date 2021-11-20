import sys
from io import StringIO

test_input_1 = """2
1, 2, 3
4, 5, 6
"""

test_input_2 = """4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67
"""

# sys.stdin = StringIO(test_input_1)


def read_matrix():
    """Returns matrix from the input integers, split by ', '"""
    matrix_rows = int(input())

    matrix = []

    for _ in range(matrix_rows):
        row = []
        for x in input().split(', '):
            row.append(int(x))
        matrix.append(row)

    return matrix


matrix = read_matrix()
even_matrix = []

for row in matrix:
    only_even = []

    for x in row:
        if x % 2 == 0:
            only_even.append(x)
    even_matrix.append(only_even)

print(even_matrix)
