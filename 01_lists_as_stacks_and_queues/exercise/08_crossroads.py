from collections import deque


def crossroads_simulation():
    green_light_duration = int(input())
    free_window_duration = int(input())

    queue = deque()
    total_cars_passed = 0

    while True:
        command = input()

        if command == "END":
            print("Everyone is safe.")
            print(f"{total_cars_passed} total cars passed the crossroads.")
            break

        if command == "green":
            time_left = green_light_duration

            while queue and time_left > 0:
                car = queue.popleft()
                car_length = len(car)

                if car_length <= time_left:
                    time_left -= car_length
                    total_cars_passed += 1
                else:
                    time_left = 0
                    remaining_time = car_length - green_light_duration

                    if remaining_time <= free_window_duration:
                        total_cars_passed += 1
                    else:
                        character_hit = car[green_light_duration + free_window_duration]
                        print("A crash happened!")
                        print(f"{car} was hit at {character_hit}.")
                        return
        else:
            queue.append(command)


crossroads_simulation()
