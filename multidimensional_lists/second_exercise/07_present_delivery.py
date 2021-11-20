def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def get_next_position(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    return row, col + 1


def get_houses_in_range(r, c, size):
    houses = []
    if not is_outside(r - 1, c, size):
        houses.append([r - 1, c])
    if not is_outside(r + 1, c, size):
        houses.append([r + 1, c])
    if not is_outside(r, c - 1, size):
        houses.append([r, c - 1])
    if not is_outside(r, c + 1, size):
        houses.append([r, c + 1])
    return houses


presents = int(input())
size = int(input())

neighborhood_matrix = []

santa_row, santa_col = 0, 0
initial_nice_kids_count = 0

for row in range(size):
    elements = input().split()
    neighborhood_matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == 'S':
            santa_row, santa_col = row, col
        elif element == 'V':
            initial_nice_kids_count += 1

nice_kids_count = initial_nice_kids_count

while True:
    command = input()

    if command == 'Christmas morning':
        break

    next_santa_row, next_santa_col = get_next_position(command, santa_row, santa_col)

    if neighborhood_matrix[next_santa_row][next_santa_col] == 'V':
        nice_kids_count -= 1
        presents -= 1

    elif neighborhood_matrix[next_santa_row][next_santa_col] == 'C':
        houses_in_range = get_houses_in_range(next_santa_row, next_santa_col, size)

        for row, col in houses_in_range:
            if neighborhood_matrix[row][col] == 'X':
                presents -= 1

            if neighborhood_matrix[row][col] == 'V':
                presents -= 1
                nice_kids_count -= 1

            neighborhood_matrix[row][col] = '-'

            if presents == 0:
                break

    neighborhood_matrix[santa_row][santa_col] = '-'
    neighborhood_matrix[next_santa_row][next_santa_col] = 'S'
    santa_row, santa_col = next_santa_row, next_santa_col

    if presents == 0:
        break

if presents == 0 and nice_kids_count > 0:
    print('Santa ran out of presents!')

for row_elements in neighborhood_matrix:
    print(' '.join(row_elements))

if nice_kids_count == 0:
    print(f'Good job, Santa! {initial_nice_kids_count} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_count} nice kid/s.')
