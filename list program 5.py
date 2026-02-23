import random
def l6():
    c=[random.randrange(1,50) for x in range(10)]
    c=c.append(-40)
    f=[((x*9/5)+32)for x in c]
    print(c,f ,sep='\n')
l6()

    
    
