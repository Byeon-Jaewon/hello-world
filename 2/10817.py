a,b,c=map(int, input().split())

if a>b :
    if b<c : 
        if c>a : print(a)
        else : print(c)
    else : print(b)
elif a<b : 
    if a<c : 
        if c>b : print(b)
        else : print(c)
    else : print(a)
else : 
    print(b)
