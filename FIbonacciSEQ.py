a=0
b=1
num=int(input("enter no upto u want fibbonacci :"))
if(num==1):
    print(a)
else:
    for i in range(1,num+1):
        c=a+b
        a=b
        b=c
        print(c) 