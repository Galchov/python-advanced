rows = int(input())

matrix = [
    [int(num) for num in input().split()]
    for row in range(rows)
]

primary_diagonal = [matrix[row_col][row_col] for row_col in range(rows)]
secondary_diagonal = [matrix[::-1][row_col][row_col] for row_col in range(rows)][::-1]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
