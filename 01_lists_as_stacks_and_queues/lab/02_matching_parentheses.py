string_data = input()

parentheses = []

for i in range(len(string_data)):
    if string_data[i] == "(":
        parentheses.append(i)
    elif string_data[i] == ")":
        start_index = parentheses.pop()
        print(string_data[start_index:i + 1])
