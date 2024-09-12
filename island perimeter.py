island = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
perimeter = 0
for i in range(len(island)):
    for j in range(len(island[i])):
        if island[i][j] == 1:
            if i == 0 or island[i-1][j] == 0:
                perimeter += 1
            if i == len(island) - 1 or island[i+1][j] == 0:
                perimeter += 1
            if j == 0 or island[i][j-1] == 0:
                if j == len(island[i]) - 1 or island[i][j+1] == 0:
                    perimeter += 1
print("Island Perimeter:", perimeter)
