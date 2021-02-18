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
    for i in a : 
        for j in a:
            if i+j==n :
                result.append([i,j])
    b=sorted(result[int(len(result)/2)])
    for i in b:
        print(i, end=' ')
    print()
