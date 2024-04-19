from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0,
}

pair_completed = False
rotation = 0

while materials and magic_levels:

    rotation += 1
    current_material = materials.pop()
    current_magic = magic_levels.popleft()

    result = current_material + current_magic

    if 100 <= result <= 199:
        gifts['Gemstone'] += 1
        rotation = 0
    elif 200 <= result <= 299:
        gifts['Porcelain Sculpture'] += 1
        rotation = 0
    elif 300 <= result <= 399:
        gifts['Gold'] += 1
        rotation = 0
    elif 400 <= result <= 499:
        gifts['Diamond Jewellery'] += 1
        rotation = 0

    if rotation == 2:
        rotation = 0
        continue

    if result < 100:
        if result % 2 == 0:
            materials.append(current_material * 2)
            magic_levels.appendleft(current_magic * 3)
            continue
        elif not result % 2 == 0:
            materials.append(current_material * 2)
            magic_levels.appendleft(current_magic * 2)
            continue
    elif result > 499:
        current_material /= 2
        materials.append(current_material)
        current_magic /= 2
        magic_levels.appendleft(current_magic)
        continue

if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or (gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0):
    pair_completed = True

if pair_completed:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join(str(x) for x in materials)}')
if magic_levels:
    print(f'Magic left: {", ".join(str(x) for x in magic_levels)}')

for gift, amount in sorted(gifts.items()):
    if amount > 0:
        print(f'{gift}: {amount}')
