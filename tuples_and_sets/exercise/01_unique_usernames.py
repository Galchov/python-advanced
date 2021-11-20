import sys
from io import StringIO

test_input_1 = """6
George
George
George
Peter
George
NiceGuy1234
"""

test_input_2 = """10
Peter
Maria
Peter
George
Steve
Maria
Alex
Peter
Steve
George
"""

# sys.stdin = StringIO(test_input_1)

n = int(input())

usernames = set()

for _ in range(n):
    username = input()

    if username not in usernames:
        usernames.add(username)
        print(username)
