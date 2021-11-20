sublists = input().split('|')

result = []

for idx in range(len(sublists) - 1, -1, -1):
    elements = sublists[idx].split()
    result += elements

print(' '.join(result))


# input_data = input().split('|')
#
# matrix = []
#
# for sub in input_data:
#     sub_matrix = sub.strip().split()
#     row = []
#
#     for el in sub_matrix:
#         row.append(int(el))
#     matrix.append(row)
#
# flatten_matrix = []
#
# for row in range(len(matrix) - 1, -1, -1):
#     for num in matrix[row]:
#         flatten_matrix.append(num)
#
# print(' '.join([str(x) for x in flatten_matrix]))
