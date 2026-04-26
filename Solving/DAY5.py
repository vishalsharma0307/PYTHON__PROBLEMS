# 13. Remove duplicates from a list (without set()).

que=[10,20,30,10,20,30,40,40,80,90,10,90]
lst=[]
index=0
for x in que:
    found=False
    for el in lst:
        if x ==el:
            found=True
            break
    if found==False:        
        lst.append(x)
        index+=1

print(lst)
         
