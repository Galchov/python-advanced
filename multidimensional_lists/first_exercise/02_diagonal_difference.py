size = int(input())

matrix = []

for _ in range(size):
    row = []
    for x in input().split():
        row.append(int(x))
    matrix.append(row)

primary = []
secondary = []
for row in range(size):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][size - 1 - row])

print(abs(sum(primary) - sum(secondary)))
