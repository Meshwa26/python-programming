def ls():
    x=int(input("enter the number"))
    y=int(input("enter the number"))

    if x>y:
        print("the largest number is",x)
        print("the smalest number is",y)
    elif x==y:
        print("both are equal")
    else:
        print("the largest number is",y)
        print("the smalest number is",x)

ls()
    
