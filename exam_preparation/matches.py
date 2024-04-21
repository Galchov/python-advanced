from collections import deque

males_list = [int(x) for x in input().split() if int(x) > 0]
females_list = deque(int(x) for x in input().split() if int(x) > 0)

matches_count = 0

while males_list and females_list:
    male = males_list.pop()
    female = females_list.popleft()

    if male % 25 == 0:
        males_list.pop()
        females_list.appendleft(female)
        continue

    if female % 25 == 0:
        females_list.popleft()
        males_list.append(male)
        continue

    if male == female:
        matches_count += 1
    else:
        if male > 2:
            males_list.append(male - 2)

print(f'Matches: {matches_count}')
if males_list:
    print(f'Males left: {(", ".join(str(x) for x in reversed(males_list)))}')
else:
    print(f'Males left: none')
if females_list:
    print(f'Females left: {", ".join(str(x) for x in females_list)}')
else:
    print(f'Females left: none')
