input_data = input().split()

reversed_numbers = []

for _ in range(len(input_data)):
    reversed_numbers.append(int(input_data.pop()))

print(' '.join([str(el) for el in reversed_numbers]))

# print(' '.join(map(str, reversed_numbers)))
