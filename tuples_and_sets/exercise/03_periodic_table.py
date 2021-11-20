import sys
from io import StringIO

test_input_1 = """4
Ce O
Mo O Ce
Ee
Mo
"""

test_input_2 = """3
Ge Ch O Ne
Nb Mo Tc
O Ne
"""

# sys.stdin = StringIO(test_input_2)

n = int(input())

periodic_table = set()

for _ in range(n):
    elements = input().split(' ')

    for el in elements:
        if el not in periodic_table:
            periodic_table.add(el)

for el in periodic_table:
    print(el)
