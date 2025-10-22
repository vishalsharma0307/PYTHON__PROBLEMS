def natural(n):
    if(n==1):
        return 1
    else:
        return n+natural(n-1)
x=int(input("enter a number :"))