def d4():
    s=input("ënter a string")
    f={}
    for ch in s:
        if ch in f.keys():
            f[ch]+=1
        else:
            f[ch]=1
    print(f)
d4()
