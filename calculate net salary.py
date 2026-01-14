def salary():
    g=int(input("enter the gross salary "))
    a=0.1*g
    d=0.03*g
    
    n=g+a-d
    
    print("the net salary is ",n)
salary()