import random
def l2():
    x=[random.randrange(100000,999999) for x in range(20)]
    print(x)
    n=int(input("enter the number"))
    if n in x:
        for i,v in enumerate(x):
            if v==n:
                print()
    else:
        print(n,"not found")

l2()
