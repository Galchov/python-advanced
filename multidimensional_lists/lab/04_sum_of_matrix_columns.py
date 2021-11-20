import sys
from io import StringIO


test_input_1 = """3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
"""

# sys.stdin = StringIO(test_input_1)


def read_matrix():
    """Returns a matrix from the input integers, split by ', '"""

    rows_columns = []
    for el in input().split(', '):
        rows_columns.append(int(el))

    n, m = rows_columns

    matrix = []

    for row_index in range(n):
        row = []

        for x in input().split(' '):
            row.append(int(x))
        matrix.append(row)

    return matrix


matrix = read_matrix()

n = len(matrix)
m = len(matrix[0])
columns_sums = [0] * m

for column in range(m):
    for row in range(n):
        value = matrix[row][column]
        columns_sums[column] += value

for x in columns_sums:
    print(x)
