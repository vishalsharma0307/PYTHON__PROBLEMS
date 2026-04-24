# 11. Write a function to check if a number is prime.
def prime (lst):
    if(lst <= 1):
        print('not a prime ')
        return
    
    for el in range(2,lst):
        if(lst%el==0):
            print('not a prime' )
            return
        
    print('prime no ')    
   

var=int(input('enter a no:'))    
prime(var)