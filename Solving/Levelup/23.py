# # 23. Count number of digits in a number (without len()).

# num=11549
# count=0
# for el in str(num):
#     count+=1

# print(count,'is the no of digits in :',num)    



num=15644
yz=num
count=0
while  num>0 :
    num= num // 10
    count+=1

print(count,'is the no of digits in :',yz) 