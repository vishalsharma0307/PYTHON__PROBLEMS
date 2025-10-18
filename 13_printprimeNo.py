lower=int(input("enter lower no:"))
upper=int(input("enter second no :"))
for num in range(lower,upper+1):
    if (num>1):
        for i in range(2,num):
            if (num%i==0):
                break
        else:             #"else" is used to do some sort of work at the end of the for loop
            print(num)




