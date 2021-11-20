def is_valid_position(row, col, rows, cols):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return False
    return True


rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    row = []
    for el in input().split():
        row.append(int(el))
    matrix.append(row)

while True:
    line = input()

    if line == 'END':
        break

    args = line.split()

    if not args[0] == 'swap' or not len(args) == 5:
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in args[1:]]

    if not is_valid_position(row1, row2, rows, columns) or not is_valid_position(row2, col2, rows, columns):
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row_elements in matrix:
        print(' '.join([str(x) for x in row_elements]))
