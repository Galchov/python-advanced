numbers = tuple(float(el) for el in input().split())

numbers_and_occurrences = {}
for num in numbers:
    if num not in numbers_and_occurrences:
        numbers_and_occurrences[num] = 0
    numbers_and_occurrences[num] += 1

[print(f"{key} - {value} times") for key, value in numbers_and_occurrences.items()]
