clothes = [int(i) for i in input().split()]    # List of clothes' values
rack_capacity = int(input())                   # The maximum capacity of one rack

racks = 1
sum_clothes = 0

while clothes:
    value = clothes.pop()
    sum_clothes += value

    if sum_clothes > rack_capacity:
        sum_clothes = value
        racks += 1

print(racks)