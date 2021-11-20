rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    row = []
    for el in input().split():
        row.append(el)
    matrix.append(row)

counter = 0
for row in range(rows - 1):
    for column in range(columns - 1):
        sym1 = matrix[row][column]
        sym2 = matrix[row][column + 1]
        sym3 = matrix[row + 1][column]
        sym4 = matrix[row + 1][column + 1]

        if sym1 == sym2 == sym3 == sym4:
            counter += 1

print(counter)
