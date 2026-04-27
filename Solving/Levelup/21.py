# 21. Find factorial of a number using a function.

def fact(va):
    if va == 1:
        return 1
    return va * fact (va-1)    
        
Di=int(input('enter no for factorial:'))
factory=fact(Di)    
print(factory,'is the factorial')


