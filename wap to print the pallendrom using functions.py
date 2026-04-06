def mrf4():
    lst=['madam','python','malyalam','maam',12321]
    nl=list(filter(lambda x:str(x)==(str(x)[::-1]),lst))
    print(lst,nl,sep="\n")
mrf4()
