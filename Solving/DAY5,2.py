# 14. Find the second largest number in a list.

lst=[10,20,5,90,50,45,45,20,68,100,200,500]
largest=lst[0]
for x in lst:
    if x>=largest :
        largest=x 
print(largest,'largest')     

secondlarge=0
for el in lst:
    if el < largest:
        secondlarge=el

print(secondlarge,'secondlarge')        