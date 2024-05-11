from collections import deque


kids_names = deque(input().split())
toss = int(input())

while len(kids_names) > 1:
    for _ in range(toss):
        kids_names.append(kids_names.popleft())
    print(f"Removed {kids_names.pop()}")

print(f"Last is {''.join(kids_names)}")
