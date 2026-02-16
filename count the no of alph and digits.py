def l3():
    str=input("enter a string consiting of alphabetes digits and special symbols")
    c=d=s=0
    for ch in str:
        if ch.isdigit():
            d=d+1
        elif ch.isalpha():
            c=c+1
        else:
            s=s+1
    print(s,d,c)
l3()
