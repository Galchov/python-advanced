n = int(input())

stack = []

for _ in range(n):
    query = input().split()
    command = int(query[0])

    if command == 1:
        number = int(query[1])
        stack.append(number)
    if len(stack) > 0:
        if command == 2:
            stack.pop()
        elif command == 3:
            print(max(stack))
        elif command == 4:
            print(min(stack))

stack.reverse()
print(', '.join([str(el) for el in stack]))

# print(', '.join(map(str, stack)))
