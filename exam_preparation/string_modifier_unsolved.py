def is_inside(size, row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def get_next_position(cmd, row, col):
    if cmd == 'right':
        return row, col + 1
    if cmd == 'left':
        return row, col - 1
    if cmd == 'up':
        return row - 1, col
    if cmd == 'down':
        return row + 1, col


some_string = input()
size = int(input())

matrix = []

# Creating the matrix:
for _ in range(size):
    row_elements = input()
    row = []
    for el in row_elements:
        row.append(el)
    matrix.append(row)

player_row, player_col = 0, 0

# Finding the player's position in the matrix:
for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'P':
            player_row, player_col = r, c

# Amount of commands you will receive:
m = int(input())

for _ in range(m):
    command = input()

    current_row, current_col = player_row, player_col
    player_row, player_col = get_next_position(command, player_row, player_col)

    if not is_inside(size, player_row, player_col):
        if not matrix[current_row][current_col] == '-':
            some_string = some_string[:-1]
            break

    value = matrix[player_row][player_col]

    if not matrix[player_row][player_col] == '-':
        some_string += value
        matrix[player_row][player_col] = 'P'
        matrix[current_row][current_col] = '-'
    else:
        matrix[player_row][player_col] = 'P'
        matrix[current_row][current_col] = '-'

print(some_string)
for row in matrix:
    print(''.join(row))
