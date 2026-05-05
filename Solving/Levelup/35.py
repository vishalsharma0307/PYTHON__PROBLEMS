# 35. Find intersection of two lists.

lst1=[2,5,8,9,5,5,1]
lst2=[5,9,8,2,2,1,4]

ls=[]
ls2=[]


for el in lst1:
    found=False
    for x in ls:
        if el ==x :
            found=True
    if found:
        pass
    else:
        ls.append(el)

print(ls)                


for em in lst2:
    found=False
    for y in ls2:
        if em ==y :
            found=True
    if found:
        pass
    else:
        ls2.append(em)

print(ls2)                

re=[]
for d in ls:
    for f in ls2:
        if d==f:
            re.append(d)

            
print(re,'is common in both list')    

############################
lst1 = [2,5,8,9,5,5,1]
lst2 = [5,9,8,2,2,1,4]

result = []

for el in lst1:
    if el in lst2 and el not in result:
        result.append(el)

print(result)