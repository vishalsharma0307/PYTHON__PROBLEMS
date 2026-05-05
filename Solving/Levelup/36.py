# 36. Find difference (elements in list1 not in list2).
lst1=[1,2,5,8,8,9,5,2]
lst2=[2,5,6,5,5,1,1]

result=[]
for el in lst1:
    if el not in lst2 and el not in result:
        result.append(el)

print(result)        


