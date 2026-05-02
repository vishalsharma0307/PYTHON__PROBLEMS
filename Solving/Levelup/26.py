# 26. Find GCD (HCF) of two numbers.

num1,num2=100,50
gcd=1
great=num1
if num2>num1:
    great=num2

for x in range(1,great):
    if (num1 % x ==0) and (num2%x==0):
        if x>gcd :
            gcd=x

print(gcd,'is the GCD of :',num1,num2)                



