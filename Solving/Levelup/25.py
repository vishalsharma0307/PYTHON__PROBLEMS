# 25. Check if a number is perfect number
# (Example: 6 → 1+2+3 = 6)

num=8
sum=0
for x in range(1,num):
    if (num%x)==0:
        sum+=x

if num==sum:
    print('is perfect number :',num)
else:
    print('is not perfect no :',num)            

