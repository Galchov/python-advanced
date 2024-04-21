def is_inside(matrix, r, c):
    """Returns True if the given indexes are not out of the given range"""

    len_matrix = len(matrix)
    if 0 <= r < len_matrix and 0 <= c < len_matrix:
        return True
    return False


def check_value(matrix):
    """Checks how many mines there are around each cell and increases the cell value by one for each mine found.
    Returns the mine field with all the cell values completed"""

    length = len(matrix)
    for r in range(length):
        for c in range(length):
            val = '*'
            if not matrix[r][c] == val:
                if is_inside(matrix, r + 1, c):  # Checking one down
                    if matrix[r + 1][c] == val:
                        matrix[r][c] += 1
                if is_inside(matrix, r - 1, c):  # Checking one up
                    if matrix[r - 1][c] == val:
                        matrix[r][c] += 1
                if is_inside(matrix, r, c + 1):  # Checking one right
                    if matrix[r][c + 1] == val:
                        matrix[r][c] += 1
                if is_inside(matrix, r, c - 1):  # Checking one left
                    if matrix[r][c - 1] == val:
                        matrix[r][c] += 1
                if is_inside(matrix, r + 1, c + 1):  # Checking diagonal down-right
                    if matrix[r + 1][c + 1] == val:
                        matrix[r][c] += 1
                if is_inside(matrix, r + 1, c - 1):  # Checking diagonal down-left
                    if matrix[r + 1][c - 1] == val:
                        matrix[r][c] += 1
                if is_inside(matrix, r - 1, c + 1):  # Checking diagonal up-right
                    if matrix[r - 1][c + 1] == val:
                        matrix[r][c] += 1
                if is_inside(matrix, r - 1, c - 1):  # Checking diagonal up-left
                    if matrix[r - 1][c - 1] == val:
                        matrix[r][c] += 1

    return matrix


size = int(input())
n = int(input())

mines_field = []

# Create a matrix of zeros representing the mines field:
for _ in range(size):
    row = [0 for col in range(size)]
    mines_field.append(row)

# Positioning the next n mines into the field:
for _ in range(n):
    location_string = input()
    location = []

    # Converting location_string into integers representing the row and column of the current mine:
    for sym in location_string:
        if sym.isdigit():
            location.append(int(sym))

    mine_row, mine_col = location

    # Place the current mine into the mines field:
    mines_field[mine_row][mine_col] = '*'

# Calling the function which calculates the final result:
final_result = check_value(mines_field)

for item in final_result:
    print(' '.join(str(x) for x in item))
