def count_lower_upper(s):
    d={'u':0,'l':0}
    for ch in st:
        if ch.isupper():
            d['u']+=1
        elif ch.islower():
            d['l']+=1
    return d
s=input("enter a string:")
print(s,count_lower_upper(s),sep="\n")
