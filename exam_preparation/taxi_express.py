from collections import deque


customers_list = deque(int(x) for x in input().split(', '))
taxis_list = [int(x) for x in input().split(', ')]

total_time = 0    # The sum of the all customer's time

while customers_list:

    if not taxis_list:
        break

    current_customer = customers_list.popleft()
    current_taxi = taxis_list.pop()

    if current_customer <= current_taxi:
        total_time += current_customer
    else:
        customers_list.appendleft(current_customer)

if not customers_list:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(x) for x in customers_list)}')
