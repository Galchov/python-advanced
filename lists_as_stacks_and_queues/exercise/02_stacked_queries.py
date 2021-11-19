lines = int(input())

stack = []

for _ in range(lines):
    query_input = input().split(' ')
    query = query_input[0]

    if query == '1':
        number = int(query_input[1])
        stack.append(number)
    elif query == '2':
        if stack:
            stack.pop()
    elif query == '3':
        if stack:
            print(max(stack))
    elif query == '4':
        if stack:
            print(min(stack))

reversed_stack = []

while stack:
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))