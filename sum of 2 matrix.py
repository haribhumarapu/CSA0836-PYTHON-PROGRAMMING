mat1=[[2,3],[4,5]]
mat2=[[7,2],[9,5]]
result=[[0,0],[0,0]]
for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        result[i][j]+=mat1[i][j]+mat2[i][j]
        print(result)
