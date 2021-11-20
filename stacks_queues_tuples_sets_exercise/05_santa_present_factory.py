from collections import deque

boxes = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

crafted = {}

while boxes and magic_values:
    box = boxes.pop()
    magic_value = magic_values.popleft()
    result = box * magic_value

    if box == 0 and magic_value == 0:
        continue

    if box == 0:
        magic_values.append(magic_value)
        continue

    if magic_value == 0:
        boxes.append(box)
        continue

    if result < 0:
        boxes.append(box + magic_value)
    elif result in presents:
        present = presents[result]

        if present in crafted:
            crafted[present] += 1
        else:
            crafted[present] = 1
    else:
        boxes.append(box + 15)

is_completed = ('Doll' in crafted and 'Wooden train' in crafted) or \
               ('Teddy bear' in crafted and 'Bicycle' in crafted)

if is_completed:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if boxes:
    print(f'Materials left: {", ".join(reversed([str(x) for x in boxes]))}')
if magic_values:
    print(f'Magic left: {", ".join([str(x) for x in magic_values])}')

for toy, magic in sorted(crafted.items()):
    print(f'{toy}: {magic}')
