lower=int(input("enter lower limit :"))
upper=int(input("enter upper limit :"))
for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while(temp>0):
        digit=temp%10
        cube=digit**order
        sum+=cube
        temp//=10
    if(sum==num):
        print("Armstronge NO is :",num)
        