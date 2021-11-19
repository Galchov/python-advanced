expression = input()

stack = []
balanced = True
pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
}

for ch in expression:
    if ch in '{[(':
        stack.append(ch)
    else:
        if not stack:
            balanced = False
            break

        last_opening_bracket = stack.pop()

        if not pairs[last_opening_bracket] == ch:
            balanced = False
            break

if balanced and not stack:
    print('YES')
else:
    print('NO')
