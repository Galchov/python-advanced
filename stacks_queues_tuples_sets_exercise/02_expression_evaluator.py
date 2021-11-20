import sys
from io import StringIO


test_input_1 = "6 3 - 2 1 * 5 /"
test_input_2 = "2 2 - 1 *"
test_input_3 = "10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *"

# sys.stdin = StringIO(test_input_1)

expression = input().split(' ')

stack = []
result = 0

for el in expression:
    if (el.strip('-')).isnumeric():
        stack.append(int(el))

    if el == "*":
        result = stack.pop(0)
        for num in stack:
            result *= num
        stack = [result]
    elif el == "+":
        result = stack.pop(0)
        for num in stack:
            result += num
        stack = [result]
    elif el == "-":
        result = stack.pop(0)
        for num in stack:
            result -= num
        stack = [result]
    elif el == "/":
        result = stack.pop(0)
        for num in stack:
            result //= num
        stack = [result]

print(result)
