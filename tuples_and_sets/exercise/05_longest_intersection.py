import sys
from io import StringIO

test_input_1 = """3
0,3-1,2
2,10-3,5
6,15-3,10
"""

test_input_2 = """5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11
"""

# sys.stdin = StringIO(test_input_2)

n = int(input())

set_one = set()
set_two = set()

intersections_list = []

for _ in range(n):
    ranges = input().split('-')
    first_range = [int(x) for x in ranges[0].split(',')]
    second_range = [int(x) for x in ranges[1].split(',')]
    first_start, first_end = first_range
    second_start, second_end = second_range

    for num in range(first_start, first_end + 1):
        set_one.add(num)

    for num in range(second_start, second_end + 1):
        set_two.add(num)

    intersection = set_one.intersection(set_two)
    intersections_list.append(list(intersection))

    set_one.clear()
    set_two.clear()

longest_intersection = []

for lst in intersections_list:
    if len(lst) > len(longest_intersection):
        longest_intersection = list(lst)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
