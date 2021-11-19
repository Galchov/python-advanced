string = input()

stack = []

for char in string:
    stack.append(char)

result = ''

while len(stack) > 0:
    result += stack.pop()

print(result)