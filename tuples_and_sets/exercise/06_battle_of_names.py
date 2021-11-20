import sys
from io import StringIO

test_input_1 = """4
Pesho
Stefan
Stamat
Gosho
"""

test_input_2 = """6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan
"""

# sys.stdin = StringIO(test_input_2)

n = int(input())
odd_set = set()
even_set = set()

rows = 1

for _ in range(n):
    name = input()

    total_sum = 0

    for letter in name:
        total_sum += ord(letter)

    total_sum = total_sum // rows

    if total_sum % 2 == 0:
        even_set.add(total_sum)
    else:
        odd_set.add(total_sum)

    rows += 1

if sum(odd_set) == sum(even_set):
    united_set = odd_set.union(even_set)
    print(*united_set, sep=', ')
if sum(odd_set) > sum(even_set):
    diff = odd_set.difference(even_set)
    print(*diff, sep=', ')
if sum(even_set) > sum(odd_set):
    symmetric_diff = odd_set.symmetric_difference(even_set)
    print(*symmetric_diff, sep=', ')
