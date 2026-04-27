# 18. Create a function that returns only even numbers from a list.

def eve (lst):
    ls=[]
    for el in lst:
        if (el%2==0):
            ls.append(el)

    return ls    

            
st=[2,5,1,10,12,22,23,25,56,89,79,17]
result=eve(st)
print(result)