numbers_list = input().split(", ")
result = 1

for i in range(len(numbers_list)):
    number = int(numbers_list[i])
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)


''' Error Code '''
# numbers_list = int(input()).split(", ")
# result = 1
#
# for i in range(numbers_list):
#     number = numbers_list[i + 1]
#     if number <= 5
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
#
# print(total)