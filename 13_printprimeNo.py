lower=int(input("enter lower no:"))
upper=int(input("enter second no :"))
y=range(2,lower)
if(lower>1):
    for x in y:
        if(y%x==0):
            break
else:
    print(lower)
for num in range(2,upper+1):
    if((upper+1)%num==0):
        break
else:
    print(num>lower)