import math


def is_inside(size, row, column):
    if 0 <= row < size and 0 <= column < size:
        return True
    return False


def get_next_position(direction, row, column):
    if direction == 'up':
        return row - 1, column
    if direction == 'down':
        return row + 1, column
    if direction == 'right':
        return row, column + 1
    if direction == 'left':
        return row, column - 1


size = int(input())

matrix = []

# Finding the player's starting position while creating the matrix:
player_row, player_col = 0, 0
for r in range(size):
    row = input().split()
    matrix.append(row)
    for c in range(size):
        element = row[c]
        if element == 'P':
            player_row, player_col = r, c

coins_counter = 0
path = []

while coins_counter < 100:
    command = input()

    if not command == 'up' and not command == 'down' and not command == 'right' and not command == 'left':
        continue

    player_row, player_col = get_next_position(command, player_row, player_col)

    if not is_inside(size, player_row, player_col) or matrix[player_row][player_col] == 'X':
        coins_counter = math.floor(coins_counter * 0.5)
        break
    else:
        coins_counter += int(matrix[player_row][player_col])
        path.append((player_row, player_col))

if coins_counter >= 100:
    print(f'You won! You\'ve collected {coins_counter} coins.')
else:
    print(f'Game over! You\'ve collected {coins_counter} coins.')

print('Your path:')
for item in path:
    print(list(item))
