# 38. Count pairs with given sum
# Input: [1,2,3,4], sum=5 → pairs (1,4),(2,3)

lst=[1,2,3,4]
dis={ }
for a in lst :
    for x in lst :
        if a+x==5 and x not in dis:
            dis[a]=x
            
        
print(dis)


