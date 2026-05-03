# 30. Check if two numbers are co-prime.

num1,num2=8,15


gcd=1
coprime=True
for x in range(2,num1+1):
    if num1%x==0 and num2%x==0 :
        coprime=False
        break

if coprime:
    print('is co-prime')    
else:
    print('not a co prime')    
    
      
        



