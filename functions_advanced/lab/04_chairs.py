def generate_combinations(values, index, count, comb):
    if len(comb) == count:
        print(', '.join(comb))
        return

    for i in range(index, len(values)):
        comb.append(values[i])
        generate_combinations(values, i + 1, count, comb)
        comb.pop()


names = input().split(', ')
chairs = int(input())

idx = 0
combinations = []

generate_combinations(names, idx, chairs, combinations)
