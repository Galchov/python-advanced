import re


def is_inside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


size = 6

matrix = []

for _ in range(size):
    matrix.append(input().split())

points_scored = 0
throws = 3
buckets_hit = []


for hit in range(throws):
    location = re.split(r'[(), ]+', input())
    row = int(location[1])
    col = int(location[2])

    if not is_inside(row, col, size) or not matrix[row][col] == 'B':
        continue

    if matrix[row][col] == 'B':
        if not [row, col] in buckets_hit:
            buckets_hit.append([row, col])
            for r in range(size):
                value = matrix[r][col]
                if value.isdigit():
                    points_scored += int(value)

if 100 <= points_scored <= 199:
    print(f"Good job! You scored {points_scored} points, and you've won Football.")
elif 200 <= points_scored <= 299:
    print(f"Good job! You scored {points_scored} points, and you've won Teddy Bear.")
elif 300 <= points_scored:
    print(f"Good job! You scored {points_scored} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - points_scored} points more to win a prize.")
