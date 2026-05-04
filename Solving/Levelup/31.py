# 31. Sum of elements at even and odd index separately.

lst=[1,2,5,5,7,8,9,10,5,51,45,65,1,4,5]
point=0
sumeve=0
sumodd=0
while point <= len(lst)-1:
    digit=0
    if point%2==0 :
        digit=lst[point]
        sumeve+=digit
        point+=1
    else:
        digit=lst[point]
        sumodd+=digit
        point+=1
print(sumeve,'as sum eve',sumodd,'as sum odd')        
