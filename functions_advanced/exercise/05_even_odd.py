def even_odd(*args):
    numbers_list = []
    command = args[-1]

    if command == 'even':
        for i in range(len(args) - 1):
            if args[i] % 2 == 0:
                numbers_list.append(args[i])

    elif command == 'odd':
        for i in range(len(args) - 1):
            if args[i] % 2 == 1:
                numbers_list.append(args[i])

    return numbers_list


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
