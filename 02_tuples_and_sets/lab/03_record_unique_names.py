count = int(input())

names_list = [input() for _ in range(count)]
unique_names = set()

for name in names_list:
    unique_names.add(name)

# Or set comprehension, instead of for loop
# unique_names = {name for name in names_list}

for name in unique_names:
    print(name)
