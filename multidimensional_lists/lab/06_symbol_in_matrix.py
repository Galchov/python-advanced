import sys
from io import StringIO


test_input_1 = """3
ABC
DEF
X!@
!
"""

test_input_2 = """4
asdd
xczc
qwee
qefw
4
"""

# sys.stdin = StringIO(test_input_1)


def read_matrix():
    """Returns a matrix formed of the input symbols"""

    n = int(input())

    matrix = []

    for _ in range(n):
        row = input()
        matrix.append(row)

    return matrix


matrix = read_matrix()
symbol = input()

is_found = False

row, column = None, None

for i in range(len(matrix)):
    if symbol in matrix[i]:
        row = i
        column = matrix[i].index(symbol)
        is_found = True
        break

if is_found:
    print(f'({row}, {column})')
else:
    print(f'{symbol} does not occur in the matrix')