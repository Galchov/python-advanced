from collections import deque

water = int(input())
users_queue = deque()
name = input()

while name != "Start":
    users_queue.append(name)
    name = input()

command = input().split()

while command[0] != "End":
    if command[0] == "refill":
        water += int(command[1])
    else:
        if int(command[0]) <= water:
            water -= int(command[0])
            print(f"{users_queue.popleft()} got water")
        else:
            print(f"{users_queue.popleft()} must wait")
    command = input().split()

print(f"{water} liters left")
