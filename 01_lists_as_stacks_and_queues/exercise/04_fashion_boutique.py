clothes = [int(item) for item in input().split() if item.isdigit()]
rack_capacity = int(input())

used_racks = [0]

while clothes:
    last_item = clothes.pop()

    if last_item + used_racks[-1] <= rack_capacity:
        used_racks[-1] += last_item
    else:
        used_racks.append(0)
        used_racks[-1] += last_item

print(len(used_racks))
