from collections import deque


def fill_cups_with_bottles(cups_input, bottles_input):
    cups = deque(map(int, cups_input.split()))
    bottles = list(map(int, bottles_input.split()))

    wasted_water = 0

    while cups and bottles:
        current_cup = cups.popleft()
        while current_cup > 0 and bottles:
            current_bottle = bottles.pop()
            if current_bottle >= current_cup:
                wasted_water += current_bottle - current_cup
                current_cup = 0
            else:
                current_cup -= current_bottle

        if current_cup > 0:
            cups.appendleft(current_cup)

    if not cups:
        remaining_bottles = " ".join(map(str, reversed(bottles)))
        print(f"Bottles: {remaining_bottles}")
    else:
        remaining_cups = " ".join(map(str, cups))
        print(f"Cups: {remaining_cups}")
    print(f"Wasted litters of water: {wasted_water}")


cups_input = "4 2 10 5"
bottles_input = "3 15 15 11 6"
fill_cups_with_bottles(cups_input, bottles_input)
