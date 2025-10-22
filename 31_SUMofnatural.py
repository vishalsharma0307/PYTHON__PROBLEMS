def natural(n):
    if(n==1):
        return 1
    else:
        return n+natural(n-1)
x=int(input("enter a number :"))
if(x==0):
    print("Enter positive NO:")
else:
    print("The sum is : ",natural(x))