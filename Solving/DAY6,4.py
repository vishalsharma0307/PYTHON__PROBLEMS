# 20. Replace all spaces in a string with -.


st='sp a c e  '
sc=list(st)
sd=[]
for el in sc:
    x=el
    if (el==" "):
        x='-'
    sd.append(x)    

se=''.join(sd)
print(se)