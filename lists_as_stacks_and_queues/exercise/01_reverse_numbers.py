numbers_string = input().split(' ')

stack = []

for _ in range(len(numbers_string)):
    stack.append(numbers_string.pop())

print(' '.join(stack))