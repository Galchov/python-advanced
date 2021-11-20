import sys
from io import StringIO

test_input_1 = """8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey
"""

# sys.stdin = StringIO(test_input_1)

n = int(input())

# names = {input() for _ in range(n)}
names = set()

for _ in range(n):
    names.add(input())

[print(name) for name in names]