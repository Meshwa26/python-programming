import math
def prime(n):
    if n==2:
        return True
    elif n% 2==0:
        return False
    else:
        for x in range(3,int(math.sqrt(n+1)),2):
            if n % x == 0:
                return False
        else:
            return True
def primefactor(n,pf=[]):
    for x in range(2,n+1):
        if n % x == 0:
            if x in pf:
                pf.append(x)
            else:
                if prime(x):
                    pf.append(x)
                    primefactor(n//x,pf)
    return pf
n=75
print(n,primefactor(n))
