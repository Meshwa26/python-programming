import operator
def t4():
    f=[('aloo puri',30),('khavsa',50),('locho',70),('timepass',40)] 
    f1=sorted(f,key=operator.itemgetter(1),reverse=True)
    print(f1)
t4()
