mat1=[[1,2],[5,3]]
mat2=[[2,3],[4,1]]
result=[[0,0],[0,0]]
for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range (len(mat2)):
           result[i][j]+=mat1[i][k]*mat2[k][j]
        for r in result:
                print(result)
                 
    
    
