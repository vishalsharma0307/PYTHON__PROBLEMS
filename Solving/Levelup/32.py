# 32. Move all zeros in a list to the end
# Input: [1,0,2,0,3] → [1,2,3,0,0]

num=[1,0,2,0,0,0,5,5,8,6,3]
index=len(num)-1
lst=[]
point=0
found=False
for el in num:
    if el == 0:

        pass
    else:
        lst.append(el)

new=len(lst)

while new <=index:
    lst.append(0)
    new+=1
    
print(lst)    
