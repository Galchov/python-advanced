rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    row = []
    for num in input().split():
        row.append(int(num))
    matrix.append(row)

max_sum = 0
best_row = 0
best_column = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        sym1 = matrix[row][column]
        sym2 = matrix[row][column + 1]
        sym3 = matrix[row][column + 2]
        sym4 = matrix[row + 1][column]
        sym5 = matrix[row + 1][column + 1]
        sym6 = matrix[row + 1][column + 2]
        sym7 = matrix[row + 2][column]
        sym8 = matrix[row + 2][column + 1]
        sym9 = matrix[row + 2][column + 2]
        current_sum = sym1 + sym2 + sym3 + sym4 + sym5 + sym6 + sym7 + sym8 + sym9

        if current_sum > max_sum:
            max_sum, best_row, best_column = current_sum, row, column

print(f'Sum = {max_sum}')
print(matrix[best_row][best_column], matrix[best_row][best_column + 1], matrix[best_row][best_column + 2])
print(matrix[best_row + 1][best_column], matrix[best_row + 1][best_column + 1], matrix[best_row + 1][best_column + 2])
print(matrix[best_row + 2][best_column], matrix[best_row + 2][best_column + 1], matrix[best_row + 2][best_column + 2])
