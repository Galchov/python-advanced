from collections import deque


total_food = int(input())
orders = deque(map(int, input().split()))

max_order = max(orders)

while orders:
    current_order = orders[0]

    if current_order > total_food:
        break
    else:
        total_food -= current_order
        orders.popleft()

print(max_order)

if orders:
    print(f'Orders left: {" ".join(map(str, orders))}')
else:
    print('Orders complete')

# from collections import deque
#
#
# food_qty = int(input())                        # Food quantity for the day
# queue = deque(map(int, input().split(' ')))    # Orders and their quantity
#
# biggest_order = 0
#
# for order in queue:
#     if int(order) > biggest_order:
#         biggest_order = int(order)
#
# print(biggest_order)
#
# while True:
#     if queue:
#         if food_qty - queue[0] >= 0:
#             food_qty -= queue.popleft()
#         else:
#             break
#     else:
#         break
#
# if queue:
#     print(f'Orders left: {" ".join(map(str, queue))}')
# else:
#     print('Orders complete')