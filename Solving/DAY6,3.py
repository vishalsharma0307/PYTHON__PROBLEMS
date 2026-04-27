# 19. Check if a string contains only digits (no .isdigit()).

st='12jnj3415'


for el in st:
    if not ('0' <= el <='9') :
        print('it has other char also ')
        break
print(' digits present')
        
