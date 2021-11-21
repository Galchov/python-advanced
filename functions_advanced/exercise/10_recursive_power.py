# def recursive_power(number, power):
#     return 2 ** 10


def recursive_power(num, power):
    if power == 1:
        return num

    return num * recursive_power(num, power - 1)


print(recursive_power(2, 10))
