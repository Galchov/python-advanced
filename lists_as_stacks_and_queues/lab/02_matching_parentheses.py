expression = input()

parentheses_indices = []

for i in range(len(expression)):
    if expression[i] == '(':
        parentheses_indices.append(i)
    elif expression[i] == ')':
        opening_index = parentheses_indices.pop()
        closing_index = i
        searched_set = expression[opening_index:closing_index + 1]
        print(searched_set)