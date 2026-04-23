# 6. Find sum of digits of a number using a loop.
nums=7874351684561200
sum=0
while(nums>0):
    digit=nums%10
    sum=sum+digit
    nums= nums//10

print(sum,'sum_as')

    
     
