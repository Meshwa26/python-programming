def s2():
    d1={108,112,74}
    d2={74,84,79}
    d3=d1&d2
    print("vistor visted both days",d3)
    d4=d1^d2
    print("vistor visted only one of the day",d4)
    d5=d1|d2
    print("total unique visitor",len(d5))
s2()
