def sosu(n) :
    s=[True]*n
    for i in range(2, int(n**0.5)+1):
        if s[i]==True :
            for j in range(2*i,n,i):
                s[j]=False
    return [i for i in range(2,n) if s[i]==True]

T=int(input())
for i in range(T):
    n=int(input())
    result=[]
    a=sosu(n)
    front=n//2
    rear=n//2
    while front>=0 : 
        if front in a and rear in a : 
            if n==front+rear : 
                print(front, rear)
                break
        front-=1
        rear+=1
