# 5. Check if a number is a palindrome.
nums= '9522126642500'
left=0
right=len(nums)-1
is_palidrome=True
while(left < right):
    if(nums[left]==nums[right]):
        left+=1
        right-=1
    else:
        is_palidrome=False
        break
        
if is_palidrome:
    print(nums,'is palidrome')
else:
    print(nums,'is not a palindrome')            


