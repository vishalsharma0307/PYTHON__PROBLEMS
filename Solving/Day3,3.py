# 7. Count how many numbers in a list are greater than 50.
list=[10,50,100,515,12115,1010,10003,112,212]
count=0
for ele in list:
    if (ele > 50):
        count+=1

print(count,'no of elements ')

