a, b = map(int, input().split())

c=45

if b>c : 
    print(a, b-c)
elif b==c : 
    print(a, 0)
else :
    if (a<1) :
        print(23, 60-(c-b))
    else :
        print(a-1, 60-(c-b))
    
