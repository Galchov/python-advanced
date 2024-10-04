from collections import deque

expression = deque(input())
OPENING_PARENTHESES = '({['
CLOSING_PARENTHESES = ')}]'
counter = 0

while expression:
    if expression[0] not in OPENING_PARENTHESES:
        break

    index = OPENING_PARENTHESES.index(expression[0])
    if expression[1] == CLOSING_PARENTHESES[index]:
        expression.popleft()
        expression.popleft()
        expression.rotate(counter)
        counter = 0
    else:
        expression.rotate(-1)
        counter += 1

if expression:
    print("NO")
else:
    print("YES")
