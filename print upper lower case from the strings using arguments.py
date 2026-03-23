def f1(str):
    d={'ú':0,'l':0}
    for x in str:
        
        if x.isupper()== True:
            d['ú']+=1
        elif x.islower()== True:
            d['l']+=1
    return d

st="PDeuSoT"
a=f1(st)
print(st,a)

        
