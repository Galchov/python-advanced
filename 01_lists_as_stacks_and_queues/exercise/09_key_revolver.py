def spy_mission():
    bullet_price = int(input())
    barrel_size = int(input())
    bullets = list(map(int, input().split()))
    locks = list(map(int, input().split()))
    intelligence_value = int(input())

    bullets_used = 0
    current_barrel = barrel_size

    while bullets and locks:
        bullet = bullets.pop()
        lock = locks[0]

        if bullet <= lock:
            print("Bang!")
            locks.pop(0)
        else:
            print("Ping!")

        bullets_used += 1
        current_barrel -= 1

        if current_barrel == 0 and bullets:
            print("Reloading!")
            current_barrel = barrel_size

    if not locks:
        bullets_left = len(bullets)
        money_earned = intelligence_value - (bullets_used * bullet_price)
        print(f"{bullets_left} bullets left. Earned ${money_earned}")
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")


spy_mission()
