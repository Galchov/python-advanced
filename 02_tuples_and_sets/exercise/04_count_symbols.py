symbols = tuple(sorted([char for char in input()]))

counted_characters = []

for symbol in symbols:

    if symbol not in counted_characters:
        print(f"{symbol}: {symbols.count(symbol)} time/s")
        counted_characters.append(symbol)
