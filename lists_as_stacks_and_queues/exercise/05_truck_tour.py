from collections import deque


queue = deque()

pumps_count = int(input())

for _ in range(pumps_count):
    pump = [int(x) for x in input().split()]
    queue.append(pump)

for i in range(pumps_count):
    car_fuel = 0
    completed = True

    for petrol, distance in queue:
        car_fuel += petrol

        if distance > car_fuel:
            completed = False
            break

        car_fuel -= distance

    if completed:
        print(i)
        break
    else:
        queue.append(queue.popleft())
