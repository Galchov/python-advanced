n = int(input())

vip_guests = set()
ordinary_guests = set()

for _ in range(n):
    guest = input()
    if guest[0].isdigit():
        vip_guests.add(guest)
    else:
        ordinary_guests.add(guest)

all_guests = sorted(list(vip_guests.union(ordinary_guests)))
arrived = set()

while True:
    arrival = input()
    if arrival == "END":
        break

    if arrival in vip_guests or arrival in ordinary_guests:
        arrived.add(arrival)

not_arrived = [g for g in all_guests if g not in arrived]
print(len(not_arrived))
print('\n'.join(not_arrived))
