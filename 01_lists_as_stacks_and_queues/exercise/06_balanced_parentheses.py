from collections import deque


def find_balanced(text):
    expression = deque(text)
    opening_parentheses = '({['
    closing_parentheses = ')}]'
    counter = 0

    while expression:
        if expression[0] not in opening_parentheses:
            break

        index = opening_parentheses.index(expression[0])
        if expression[1] == closing_parentheses[index]:
            expression.popleft()
            expression.popleft()
            expression.rotate(counter)
            counter = 0
        else:
            expression.rotate(-1)
            counter += 1

    if expression:
        return "NO"
    else:
        return "YES"


# text = deque(input())
print(find_balanced('{{[[(())]]}}'))
print(find_balanced('{[(])}'))
print(find_balanced('{[()]}'))
