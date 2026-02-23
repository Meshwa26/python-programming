import random
def list1():
    odd=[random.randrange(1,100,2)for x in range(5)]
    even=[random.randrange(2,100,2)for x in range(4)]
    print("odd number",odd)
    print("even number",even)
    odd[2]=even
    print("ödd number update",odd)
    newlist=[]
    newlist.append(v) if type(v)==int else newlist.extend(v)  for v in odd:
    
        
    #for v in odd:
       # newlist.append(v) if type(v)==int else newlist.extend(v)
        #if type(v)==int:
         #   newlist.append(v)
        #else:
         #   newlist.extend(v)
    print("flatterned list",newlist)
    newlist.sort()
    sortnewlist=sorted(newlist,key=None,reverse=True)
    print("sorted list",newlist)
    print("new sorted list",sortnewlist)
list1()
