import sys
from io import StringIO

test_input_1 = '-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'
test_input_2 = '2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3'

# sys.stdin = StringIO(test_input_2)

numbers = [float(x) for x in input().split(' ')]
numbers_counts = {}

for number in numbers:
    if number not in numbers_counts:
        numbers_counts[number] = 0
    numbers_counts[number] += 1

for num, count in numbers_counts.items():
    print(f'{num} - {count} times')

# Another solution below:

# numbers = [float(item) for item in input().split(' ')]
# numbers_tuple = tuple(numbers)
#
# checked = []
#
# for num in numbers_tuple:
#     if num not in checked:
#         checked.append(num)
#         print(f'{num:.1f} - {numbers_tuple.count(num)} times')
