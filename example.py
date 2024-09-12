list1=[1,3,5,6]
list2=[2,4,7,8]
sorted_list=[]
i,j=0,0
while i< len(list1) and j<len(list2):
    if list1[i] < list2[j]:
        sorted_list.append(list1[i])
        i += 1
    else:
        sorted_list.append(list2[j])
        j += 1
while i < len(list1):
    sorted_list.append(list1[i])
    i += 1
while i <len(list2):
    sorted_list.append(list2[j])
    j += 1
print(sorted_list)
            
    
