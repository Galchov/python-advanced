from collections import deque


jobs_sequence = [int(x) for x in input().split(', ')]
target_index = int(input())

cycles = deque(sorted([(jobs_sequence[index], index)for index in range(len(jobs_sequence))]))
result = 0

while cycles:
    number, index = cycles.popleft()
    result += number

    if index == target_index:
        print(result)
        break
