def hcf(x,y):
    if(x>y):
        small=y
        return y
    else:
        small=x
        return x
a=int(input("Enter first NO:"))
b=int(input("Enter Second NO:"))
c=hcf(a,b)
print(c)

for i in range(1,c+1):
    if((a%i==0)and(b%i==0)):
        gcd=i
else:
    print(gcd,"Is the gcd or hcf ")



