n = int(input())

parking = set()

for _ in range(n):
    data = tuple(input().split(', '))
    direction, plate = data
    if direction == "IN":
        parking.add(plate)
    elif direction == "OUT" and plate in parking:
        parking.remove(plate)

print("Parking Lot is Empty" if not parking else '\n'.join(parking))
