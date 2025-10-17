lower=int(input("enter lower no:"))
upper=int(input("enter second no :"))
if(lower==1):
    print("not a prime")
if(lower>1):
    for el in range(2,lower):
        if(lower%el==0):
            print("is not a prime ")
            break
    else:
        print("Is a prime  :",lower)
num=lower
if(num<=upper+1):
    for num in range(lower,upper+1):
            for i in range(2,upper+1):
                if(num%i==0):
                    print("Not a prime ")
                    break
    else:
         print("IS prime,",num)     




