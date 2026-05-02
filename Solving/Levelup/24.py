# 24. Reverse a number
# Input: 1234 → Output: 4321

num=123456789
sub=num
count=0
while num>0:
    num=num//10
    count+=1
  
pow=count-1
out=0
while pow >=0 :
    result=10**pow
    pow = pow-1
    while sub>0:
        digit=0
        digit =sub%10
        out+=result*digit
        sub=sub//10
        break
print(out)   
        



