# 16. Count frequency of each element in a list (return dictionary).

ques=[2,2,2,5,5,2,3,3,3,4,4,2,6,5,6,5,5,8]
lst=[]
for x in ques:
    found=False
    for el in lst:
        if x==el:
            found=True

    if found==False:
        lst.append(x) 
     

dis={
}
for v in lst:
    count=0
    for y in ques:
        if v==y:
            count+=1
    dis[v]=count

print(dis)





            


