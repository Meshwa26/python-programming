import random
def l3():
    l=[random.randrange(1,99) for x in range(50)]
    print(l)
    nl=[]
    for v in l:
        if v not in nl:
            nl.append(v)
    print(nl)
l3()
