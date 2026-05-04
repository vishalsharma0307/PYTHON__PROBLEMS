# 33. Find missing number in list
# Input: [1,2,4,5] → Output: 3


lst=[1,2,3,5,6,7,9]
point=0
var=lst[point]
for el in lst:
    if el == var:
        var+=1
    elif el==var+1:
        print(var,end=', ')
        var+=2