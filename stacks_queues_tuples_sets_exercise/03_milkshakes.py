import sys
from io import StringIO
from collections import deque

test_input_1 = """20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55
"""

test_input_2 = """-10, -2, -30, 10
-5
"""

test_input_3 = """2, 3, 3, 7, 2
2, 7, 3, 3, 2, 14, 6
"""

sys.stdin = StringIO(test_input_1)

chocolate = [int(el) for el in input().split(', ')]
milk = deque(int(el) for el in input().split(', '))

milkshakes = 0

while len(milk) > 0 and len(chocolate) > 0:
    choco_cup = chocolate.pop()
    milk_cup = milk.popleft()

    if choco_cup <= 0 or milk_cup <= 0:
        if choco_cup > 0:
            chocolate.append(choco_cup)
        if milk_cup > 0:
            milk.appendleft(milk_cup)
    elif choco_cup == milk_cup:
        milkshakes += 1
    else:
        milk.append(milk_cup)
        chocolate.append(choco_cup - 5)

    if milkshakes == 5:
        print("Great! You made all the chocolate milkshakes needed!")
        break

if milkshakes < 5:
    print("Not enough milkshakes.")
if len(chocolate) > 0:
    print(f'Chocolate: {", ".join([str(el) for el in chocolate])}')
else:
    print("Chocolate: empty")
if len(milk) > 0:
    print(f'Milk: {", ".join([str(el) for el in milk])}')
else:
    print('Milk: empty')
