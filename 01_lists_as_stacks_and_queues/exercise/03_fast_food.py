from collections import deque


day_food_qty = int(input())
orders_sequence = deque(int(order) for order in input().split() if order.isdigit())

# Or for slightly better readability use the code below
#
# orders_sequence_input = input().split()
# orders_sequence = deque()
# for order in orders_sequence_input:
#     if order.isdigit():
#         orders_sequence.append(int(order))

biggest_order = 0
for order in orders_sequence:
    if order > biggest_order:
        biggest_order = order

# Or simpy use 'max(orders_sequence)'

print(biggest_order)

not_enough_food = False
while orders_sequence:
    next_order = orders_sequence[0]

    if day_food_qty - next_order >= 0:
        day_food_qty -= orders_sequence.popleft()
    else:
        not_enough_food = True
        break

if not_enough_food:
    print(f"Orders left: {' '.join(map(str, orders_sequence))}")
else:
    print("Orders complete")
