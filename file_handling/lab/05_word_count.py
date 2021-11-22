import re
import string

with open('words.txt') as file:
    searched_words = file.read().split()

occurrences = {}

with open('input.txt') as file:
    content = file.read().lower()
    for searched_word in searched_words:
        result = re.findall(f"{searched_word}", content)
        occurrences[searched_word] = len(result)

sorted_result = sorted(occurrences.items(), key=lambda x: -x[1])
for key, value in sorted_result:
    print(f'{key} - {value}')
