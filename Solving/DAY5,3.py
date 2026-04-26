# 15. Check if a string is a palindrome (use function)

def palindrome (st):
    left=0
    right=len(st)-1
    palindro=True
    while left < right :
        if st[left]==st[right] :
            left+=1
            right-=1
            palindro=True
        else:
            palindro=False
            break

    if palindro:
        print('is a palindrome')
    else:
        print('is not a palindrome')    
     
    
sc='racecar'
result=palindrome(sc)
