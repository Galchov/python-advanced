from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar_values = [int(x) for x in input().split()]
operative_symbols = deque(input().split())

total_honey = 0

while working_bees and nectar_values:
    current_bee = working_bees.popleft()
    current_nectar = nectar_values.pop()

    if current_nectar >= current_bee:
        sym = operative_symbols.popleft()

        if sym == '+':
            total_honey += abs(current_bee + current_nectar)
        elif sym == '-':
            total_honey += abs(current_bee - current_nectar)
        elif sym == '*':
            total_honey += abs(current_bee * current_nectar)
        elif sym == '/':
            if current_nectar > 0:
                total_honey += abs(current_bee / current_nectar)
    else:
        working_bees.appendleft(current_bee)

print(f'Total honey made: {total_honey}')

if working_bees:
    print(f'Bees left: {", ".join(str(x) for x in working_bees)}')
if nectar_values:
    print(f'Nectar left: {", ".join(str(x) for x in nectar_values)}')
