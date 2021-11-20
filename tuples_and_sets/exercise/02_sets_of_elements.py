import sys
from io import StringIO

test_input_1 = """4 3
1
3
5
7
3
4
5
"""

test_input_2 = """2 2
1
3
1
5
"""

# sys.stdin = StringIO(test_input_1)

sets_length = [int(num) for num in input().split(' ')]

n, m = sets_length
set_n = set()
set_m = set()

counter = 0

for _ in range(n + m):
    element = int(input())
    counter += 1

    if counter <= n:
        set_n.add(element)
    else:
        set_m.add(element)

mutual_elements = set_n.intersection(set_m)

for el in mutual_elements:
    print(el)
