matrix = [[4,5,6],
          [7,8,9],
          [1,2,3]]
transpose = []
for i in range(len(matrix[0])):
    row = []
    for row_num in matrix:
        row.append(row_num[i])
    transpose.append(row)

print(transpose)
