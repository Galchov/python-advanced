from collections import deque


def is_ready(show_fireworks):
    """Returns True if all the values in the dictionary are equal to 3 or above"""

    return all(x >= 3 for x in show_fireworks.values())


def print_fireworks(fireworks, explosives, show_fireworks_dict):
    """Prints fireworks and/or explosives if there are any left
    and at the end prints the values of the fireworks dictionary"""

    if fireworks:
        print(f'Firework Effect left: {", ".join(str(x) for x in fireworks)}')
    if explosives:
        print(f'Explosive Power left: {", ".join(str(x) for x in explosives)}')
    print(f'Palm Fireworks: {show_fireworks_dict["palm"]} \n'
          f'Willow Fireworks: {show_fireworks_dict["willow"]} \n'
          f'Crossette Fireworks: {show_fireworks_dict["crossette"]}')


firework_effects = deque(int(x) for x in input().split(', ') if int(x) > 0)
explosive_powers = [int(x) for x in input().split(', ') if int(x) > 0]

show_fireworks = {
    'palm': 0,
    'willow': 0,
    'crossette': 0,
}

while firework_effects and explosive_powers and not is_ready(show_fireworks):
    firework = firework_effects.popleft()
    explosive = explosive_powers.pop()
    current_sum = firework + explosive

    if current_sum % 3 == 0 and current_sum % 5 == 0:
        show_fireworks['crossette'] += 1
    elif current_sum % 3 == 0:
        show_fireworks['palm'] += 1
    elif current_sum % 5 == 0:
        show_fireworks['willow'] += 1
    else:
        if firework > 1:
            firework_effects.append(firework - 1)
        explosive_powers.append(explosive)

if is_ready(show_fireworks):
    print("Congrats! You made the perfect firework show!")
    print_fireworks(firework_effects, explosive_powers, show_fireworks)
else:
    print("Sorry. You can't make the perfect firework show.")
    print_fireworks(firework_effects, explosive_powers, show_fireworks)
