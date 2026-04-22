# 3. Find the largest element in a list (no max()).

def largest (lst):
    highest =0
    for el in lst:
        if (el > highest ):
            highest=el
        
    return highest    

nums=[50,100,20,10,80,90,30]    
high= largest(nums)
print(high,"highest_number") 