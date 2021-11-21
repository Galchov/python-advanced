def multiply(*args):
    """Returns the multiplication result of random amount of numbers given"""

    if not args:
        return None

    product = 1
    for x in args:
        product *= x

    return product
