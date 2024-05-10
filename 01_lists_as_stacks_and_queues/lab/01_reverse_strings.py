string_data = list(input())

stack = []

for _ in range(len(string_data)):
    stack.append(string_data.pop())

print(''.join(stack))
