def t7():
    f=('aloo puri','khavsa','locho','timepass')
    print(f)
    f1=input("ënter a fooditeam")
    f1l1=[]
    if f1 in f:
        for i in f:
            if i!=f1:
                f1l1.append(i)

        f1l1=tuple(f1l1)
    else:
        f1l1=f
        
    print(f1l1)
t7()
