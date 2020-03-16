import math
def sosu(n) :
    s=[True]*n
    m=int(math.sqrt(n))
    for i in range(2,m+1):
       if s[i]==True:
           for j in range(i+i,n,i):
               s[j]=False
    return [i for i in range(2,n) if s[i]==True]
while 1 :
    count=[]
    N=int(input())
    if N==0 : break
    count=sosu(N)
    print(len(count))

