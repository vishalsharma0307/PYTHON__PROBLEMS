# 1. Write a function to count even and odd numbers in a list.
def even_odd (lst):
        count_even=0
        count_odd=0
        for x in lst:
            if(x%2 ==0):
                count_even+=1
                
            else:
                count_odd+=1

        
        print(count_odd,"odd count",count_even,"even count")                  
       
temp=[1,2,3,4,5,6,8,10,]
even_odd(temp)



    



