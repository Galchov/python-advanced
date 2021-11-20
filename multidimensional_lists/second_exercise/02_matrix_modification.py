def is_invalid_position(size, row, col):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()

    if line == 'END':
        break
    args = line.split()
    command = args[0]
    row, col, value = [int(x) for x in args[1:]]

    if is_invalid_position(size, row, col):
        print('Invalid coordinates')
        continue

    if command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value

for row_elements in matrix:
    print(' '.join([str(x) for x in row_elements]))


# def is_valid(row, column, matrix_length):
#     return 0 <= row < matrix_length and 0 <= column < matrix_length
#
#
# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     r = []
#     for column in input().split():
#         r.append(int(column))
#     matrix.append(r)
#
# while True:
#     command_args = input().split()
#     command = command_args[0]
#
#     if command == 'END':
#         break
#
#     row = int(command_args[1])
#     col = int(command_args[2])
#     value = int(command_args[3])
#
#     if not is_valid(row, col, len(matrix)):
#         print('Invalid coordinates')
#         continue
#
#     if command == 'Add':
#         matrix[row][col] += value
#     elif command == 'Subtract':
#         matrix[row][col] -= value
#
# for row in matrix:
#     for el in row:
#         print(el, end=' ')
#     print()
