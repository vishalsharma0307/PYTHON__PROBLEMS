# 22. Check if a number is an Armstrong number
# (Example: 153 → 1³ + 5³ + 3³ = 153)

number =371
le=len(str(number))
print(le)
sum=0
input_=number
digit=0
while number > 0 :
    digit=number % 10
    sum+=digit**le
    number=number//10


if sum==input_:
    print(input_,'is an armstronge number ')
else:
    print(input_,'is not a armstronge')
    
