import random
def addlist3():
    l=[random.randrange(-15,15)for x in range(10)]
    print(l)
    l2=list(map((lambda x:x*x),l))
    print(l2)
                           
addlist3()
    
    
