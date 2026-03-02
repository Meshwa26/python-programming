def t1 ():
    s=['anurakti',('Datt',),'meshwa',('shivom','aryan')]
    b=g=0
    for x in s:
        if isinstance(x,tuple):
            b=b+len(x)
        else:
            g=g+1
    print("total student",s)
    print("boys",b)
    print("girls",g)
t1()
