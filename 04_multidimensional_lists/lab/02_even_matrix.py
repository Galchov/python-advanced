rows = int(input())

matrix = []
even_matrix = []

for row in range(rows):
    columns = list(map(int, input().split(", ")))
    matrix.append(columns)

[even_matrix.append([num for num in matrix[row] if num % 2 == 0]) for row in range(rows)]

print(even_matrix)
