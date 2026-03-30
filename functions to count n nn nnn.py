def count(n):
    s,t=0,0
    for x in range(4):
        t=t*10+n
        s+=t
    return s

for v in range(4,8):
    print(v, count(v))
    
