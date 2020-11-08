N=int(input())
for _ in range(N) :
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    a=((x1-x2)**2+(y1-y2)**2)**0.5
    if a==0 and r1==r2 : print(-1)
    elif r1+a >r2 and r2+a>r1 and r1+r2>a :
        print(2)
    elif r1+a==r2 or r2+a==r1 or r1+r2==a :
        print(1)
    else : print(0)
