# Fibonacci
# f(n) = f(n - 1) + f(n - 2)
# f(1) = f(0) = 0


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
