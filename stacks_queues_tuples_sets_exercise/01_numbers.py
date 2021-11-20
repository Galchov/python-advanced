import sys
from io import StringIO

test_input_1 = """1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset
"""

test_input_2 = """5 4 2 9 9 5 4
1 1 1 5 6 5
4
Add First 5 6 9 3
Add Second 1 2 3 3 3
Check Subset
Remove Second 1 2 3 4 5
"""

# sys.stdin = StringIO(test_input_2)

first_sequence = {int(x) for x in input().split(' ')}
second_sequence = {int(x) for x in input().split(' ')}

n = int(input())

for _ in range(n):
    command = input().split(' ')
    command_start = command[0]
    command_arg = command[1]

    if command_start == "Add":
        if command_arg == "First":
            for el in command:
                if el.isnumeric() and int(el) not in first_sequence:
                    first_sequence.add(int(el))
        elif command_arg == "Second":
            for el in command:
                if el.isnumeric() and int(el) not in second_sequence:
                    second_sequence.add(int(el))
    elif command_start == "Remove":
        if command_arg == "First":
            for el in command:
                if el.isnumeric() and int(el) in first_sequence:
                    first_sequence.remove(int(el))
        elif command_arg == "Second":
            for el in command:
                if el.isnumeric() and int(el) in second_sequence:
                    second_sequence.remove(int(el))
    elif command_start == "Check":
        if first_sequence.issubset(second_sequence):
            print(first_sequence.issubset(second_sequence))
        elif second_sequence.issubset(first_sequence):
            print(second_sequence.issubset(first_sequence))
        else:
            print(False)

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
