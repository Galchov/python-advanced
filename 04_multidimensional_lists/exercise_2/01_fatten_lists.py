matrix = [nums.split() for nums in input().split("|")]
[[print(value, end=" ") for value in lst] for lst in matrix[::-1]]
