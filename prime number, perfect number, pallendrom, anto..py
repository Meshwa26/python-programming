def l4():
    
    n=int(input("enter the number"))
    s=0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            s=s+i
    print("perfect") if n==s else print("not perfect")


    s=0
    t=n
    while t:
        r=t%10
        s=s+r*r*r
        t=int(t/10)
    print("armstrong") if s==n else print("not armstrong")

    s=n*n
    ln=len(str(n))
    div=int("1"+("0"*ln))
    r = s % div
    print("automorphic") if r==n else print("not automorphic")

    print("pallindrome") if str(n)==str(n)[::-i] else print("not pallindrome")     
    
    if n<1:
        print("invalid number")
    elif n==0 or  n==1:
        print("ho ho! why are you wasting my time?")
    elif n==2:
        print("prime")
    elif n % 2==0:
        print("not prime")
    else:
        isprime='y'
        for d in range(3,n+1,2):
            if n%d==0:
                isprime ='n'
        print("prime") if isprime == 'n' else print ("not prime")
l4()
