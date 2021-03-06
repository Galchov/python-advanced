import sys
from io import StringIO

test_input_1 = """5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END
"""

test_input_2 = """6
m8rfQBvl
fc1oZCE0
UgffRkOn
7ugX7bm0
9CQBGUeJ
2FQZT3uC
2FQZT3uC
9CQBGUeJ
fc1oZCE0
END
"""

# sys.stdin = StringIO(test_input_1)

n = int(input())

guest_list = {input() for _ in range(n)}

while True:
    command = input()

    if command == 'END':
        break

    guest_list.remove(command)


def is_vip(guest):
    return guest[0].isdigit()


vip_guests = sorted([g for g in guest_list if is_vip(g)])

regular_guest = sorted([g for g in guest_list if not is_vip(g)])

print(len(guest_list))
[print(g) for g in vip_guests]
[print(g) for g in regular_guest]
