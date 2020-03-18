import math
def sosu(n) :
    s=[True]*n
    if n==1 : return []
    for i in range(2, int(math.sqrt(n))+1):
        if s[i]==True :
            for j in range(2*i,n,i):
                s[j]=False
    return [i for i in range(2,n) if s[i]==True]

while 1:
    n=int(input())
    if n==0 : break
    c=sosu(2*n+1)
    print(len([i for i in c if i>n]))
