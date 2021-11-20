rows, columns = [int(x) for x in input().split()]
word = input()

matrix = []
word_index = 0

for row in range(rows):
    matrix.append([None] * columns)

    for column in range(columns):
        if row % 2 == 0:
            matrix[row][column] = word[word_index]
        else:
            matrix[row][columns - 1 - column] = word[word_index]
        word_index = (word_index + 1) % len(word)

for elements in matrix:
    print(''.join(elements))
