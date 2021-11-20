import sys
from io import StringIO

test_input = """3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
"""

# sys.stdin = StringIO(test_input)


def read_matrix():
    """Returns a matrix from the input integers, split by ', '"""

    rows_columns_list = []
    for x in input().split(', '):
        rows_columns_list.append(int(x))

    n, m = rows_columns_list

    matrix = []

    for _ in range(n):
        row = []
        for x in input().split(', '):
            row.append(int(x))
        matrix.append(row)

    return matrix


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])
the_sum = 0

for row_index in range(n):
    row = matrix[row_index]
    the_sum += sum(row)

print(the_sum)
print(matrix)