# 34. Merge two lists without duplicates.
lst1=[1,2,5,8,9,3,7,5,6,6]
lst2=[2,5,9,6,6,5,11,2,10]
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

small=0
if len(ls)>len(ls2):
    small=ls2           
else:
    small=ls     
            


# result=[]
# for z in ls:
#     res=False
#     for w in ls2:
#         if z==w :
#             res=True
#     if res:
#         pass
#     else:
#         result.append(z)      
# for e in ls2:
#     re=False
#     for r in ls:
#         if e==r:
#             re=True
#     if re:
#         pass
#     else:
#         result.append(e)                

# print(result,'-> is the result of unique items in both the list','(A − B) ∪ (B − A)')
result = []

for el in ls:
    if el not in result:
        result.append(el)

for el in ls2:
    if el not in result:
        result.append(el)

print(result,'is the list as A U B')