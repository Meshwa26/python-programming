def f2(str):
    alph=set('abcdefghijklmnopqrstuvwxyz')
    setstr=set(str)
    #print(set(alph),"is","" if f2()
    return setstr<=alph
print("ä","is pangram:",f2("a"))
str="the quick brown fox jumpes over the lazy dog is pangram?"
print(str,"is pangram:",f2(str))

print("ä","is pangram:","yes" if f2("a") else "no")
str="the quick brown fox jumpes over the lazy dog is pangram?"
print(str,"is pangram:","yes" if f2(str) else "no")
