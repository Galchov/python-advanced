rows = int(input())

matrix = []

for row in range(rows):
    columns = list(map(int, input().split(", ")))
    matrix.append(columns)

flattening_matrix = []
[[flattening_matrix.append(num) for num in matrix[row]] for row in range(rows)]

print(flattening_matrix)
