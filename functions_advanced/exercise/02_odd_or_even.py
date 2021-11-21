command = input()
numbers_sequence = [int(x) for x in input().split()]

odd_numbers = []
even_numbers = []

for number in numbers_sequence:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

if command == 'Odd':
    print(sum(odd_numbers) * len(numbers_sequence))
elif command == 'Even':
    print(sum(even_numbers) * len(numbers_sequence))
