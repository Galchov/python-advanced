from collections import deque

pizza_orders = deque(int(x) for x in input().split(', ') if int(x) > 0)
employees_capacity = deque(int(x) for x in input().split(', '))

orders_completed = 0

while pizza_orders and employees_capacity:
    current_order = pizza_orders.popleft()
    current_employee_capacity = employees_capacity.pop()

    if current_order <= 10:
        if current_order <= current_employee_capacity:
            orders_completed += current_order
        else:
            orders_completed += current_employee_capacity
            pizza_orders.appendleft(current_order - current_employee_capacity)
    else:
        employees_capacity.append(current_employee_capacity)

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {orders_completed}')
    print(f'Employees: {", ".join(str(x) for x in employees_capacity)}')
if not employees_capacity:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in pizza_orders)}')
