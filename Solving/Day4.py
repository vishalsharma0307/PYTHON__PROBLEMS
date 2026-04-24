# 9. Find the smallest number in a list.
lst=[30,40,50,10,5,20,60,7]
small=lst[0]
for el in lst:
    if el < small :
        small=el

print(small,'is smallest  no ')        
