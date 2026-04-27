# 17. Find common elements between two lists.

lst=[5,10,15,20,25,30,35,40,45,50,55,60]
lst2=[25,35,45,55,75,85]

for el in lst2:
    common=False
    for x in lst:
        if x==el :
            common=True
    if common :
        print(el,end=" ")        
        