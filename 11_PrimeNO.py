num=int(input('Enter a Number :'))
if(num==1):
    print("NO is not Prime.")
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print('IS not a Prime.')
            break
    else:
        print("IS A PRIME NUMBER .")
            
