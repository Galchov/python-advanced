numbers = [int(x) for x in input().split()]

negatives_sum = 0
positives_sum = 0

for num in numbers:
    if num < 0:
        negatives_sum += num
    elif num > 0:
        positives_sum += num

print(negatives_sum)
print(positives_sum)

if abs(negatives_sum) > abs(positives_sum):
    print('The negatives are stronger than the positives')
elif abs(negatives_sum) < abs(positives_sum):
    print('The positives are stronger than the negatives')
