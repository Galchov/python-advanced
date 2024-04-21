from collections import deque


def is_equal(the_sum: int, bombs: dict):
    for key, value in bombs.items():
        if value == the_sum:
            return key


def ready_to_bomb(bombs):
    return all(x >= 3 for x in ready_bombs.values())


bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = [int(x) for x in input().split(', ')]

bombs_requirements = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120,
}

ready_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

while bomb_effects and bomb_casings:
    current_bomb_effect = bomb_effects.popleft()
    current_bomb_casing = bomb_casings.pop()
    current_sum = current_bomb_effect + current_bomb_casing

    if is_equal(current_sum, bombs_requirements):
        bomb = is_equal(current_sum, bombs_requirements)
        ready_bombs[bomb] += 1
    else:
        bomb_casings.append(current_bomb_casing - 5)
        bomb_effects.appendleft(current_bomb_effect)

    if ready_to_bomb(ready_bombs):
        break

if ready_to_bomb(ready_bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f'Bomb Effects: {", ".join(str(x) for x in bomb_effects)}')
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join(str(x) for x in bomb_casings)}')
else:
    print('Bomb Casings: empty')

print(f'Cherry Bombs: {ready_bombs["Cherry Bombs"]} \n'
      f'Datura Bombs: {ready_bombs["Datura Bombs"]} \n'
      f'Smoke Decoy Bombs: {ready_bombs["Smoke Decoy Bombs"]}')
