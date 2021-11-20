import sys
from io import StringIO

test_input_1 = "SoftUni rocks"

test_input_2 = "Why do you like Python?"

# sys.stdin = StringIO(test_input_1)

text = input()

text_as_tuple = tuple(text)

symbols_dict = {}

for sym in text:
    if sym not in symbols_dict:
        symbols_dict[sym] = text_as_tuple.count(sym)

sorted_dict = sorted(symbols_dict.items(), key=lambda x: x[0])

for key, value in sorted_dict:
    print(f"{key}: {value} time/s")
