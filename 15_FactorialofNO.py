
#sol 1 by loops

# num= int(input("enter a number:"))
# fact=1
# if(num<0):
#     print("factorial is not defined")
# if(num==0):
#     print("factorial of 0 is 1")
# if(num>0):
#     for i in range(1,num+1):
#         fact=fact*i
#     else:
#         print("the factorial of num is :",fact)

#sol 2 by recursion

def fact(a):
    if(a==0):
        return 1
    else:
        return (a * fact(a-1))
num=int(input("enter a number :"))
result=fact(num)
print("the factorial is : ,",result)

