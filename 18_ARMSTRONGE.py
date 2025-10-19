num=int(input("enter a number :"))
order=len(str(num))
sum=0
temp=num
x=num
while(temp>0):
    digit=temp%10
    cube=digit**order
    sum=sum+cube
    temp//=10     # Use integer division
if(sum==x):
    print("IT is an armstronge number:")
else:
    print("IS not a armstronge number:")


