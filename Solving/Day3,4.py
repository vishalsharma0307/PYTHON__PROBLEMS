# 8. Convert a string to uppercase without using .upper().
st='vishal shArma'
upper=''
for el in st:
    if ('a'<= el <= 'z'):
        upper+=chr(ord(el)-32)
    elif('A'<= el <= 'Z'):
        upper+=el    
    else:
        upper+=el    

print(upper)