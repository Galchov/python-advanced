from collections import deque

water_qty = int(input())

queue = deque()

while True:
    command = input()
    if command == 'Start':
        break

    queue.append(command)

while True:
    command = input()
    if command == 'End':
        break

    elif command.startswith('refill'):
        cmd_args = command.split()
        liters = int(cmd_args[1])
        water_qty += liters

    else:
        person = queue.popleft()
        water_required = int(command)

        if water_required <= water_qty:
            print(f'{person} got water')
            water_qty -= water_required
        else:
            print(f'{person} must wait')

print(f'{water_qty} liters left')
