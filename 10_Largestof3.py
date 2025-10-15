
while True:
    a=int(input("Enter first No :"))
    b=int(input("Enter second No :"))
    c=int(input("Enter third No :"))
    if((a>b)and(b>c)):
        print(a,"Is largest")
    elif((b>c)and(b>a)):
        print(b,"Is largest")
    else:
        print(c,"IS largest")
