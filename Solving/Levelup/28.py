# 28. Print all prime numbers between 1 to N.
       
num = 50

for el in range(2, num + 1):
    is_prime = True

    for x in range(2, el):
        if el % x == 0:
            is_prime = False
            break

    if is_prime:
        print(el ,end=' ' "is prime ,")   
   

        
       

