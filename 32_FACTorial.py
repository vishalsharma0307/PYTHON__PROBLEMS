def fact(n):
    if(n==1):
        return 1
    else:
        return(n * fact(n-1))
n=int(input("Enter the Number :"))
if(n<=0):
    print("Factorial of number less than 1 does not exsits :")
else:
    print("factorial of given Number is :",fact(n))