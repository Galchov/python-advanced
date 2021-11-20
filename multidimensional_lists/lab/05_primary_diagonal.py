import sys
from io import StringIO


test_input_1 = """3
11 2 4
4 5 6
10 8 -12
"""

test_input_2 = """3
1 2 3
4 5 6
7 8 9
"""

# sys.stdin = StringIO(test_input_1)


def read_matrix():
    """Returns a matrix formed of the input integers, split by ', '"""

    n = int(input())

    matrix = []

    for _ in range(n):
        row = []
        for x in input().split(' '):
            row.append(int(x))
        matrix.append(row)

    return matrix


matrix = read_matrix()

n = len(matrix)
primary_sum = 0

for i in range(n):
    el = matrix[i][i]
    primary_sum += el

print(primary_sum)