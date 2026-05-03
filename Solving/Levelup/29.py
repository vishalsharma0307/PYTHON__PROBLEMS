# 29. Count frequency of digits in a number
# Input: 112233 → {1:2,2:2,3:2}

num=112233
sub=num
uniq=[]
dic={}
while num>0:
    digit=0
    digit=num%10
    num=num//10
    found=False
    for el in uniq:
        if digit==el :
            found=True
    if found==False:
        uniq.append(digit)
      
for y in uniq:
    freq=0
    rancho=sub
    while rancho>0:
        digit=0
        digit=rancho%10
        rancho=rancho//10
        if y==digit:
            freq+=1    
    dic[y]=freq

print(dic)       

             


