def s1():
    a={'maths','physics','çhemistry'}
    b={'physics','biology','maths'}
    c=a.intersection(b)
    print("common subject",c)
    c1=a&b
    print("common subject",c)
    d=a-b
    print("önly subject of a",d)
    e=b-a
    print("önly subject of b",e)
    f=a|b
    print("total no of elements",len(f))
s1()
