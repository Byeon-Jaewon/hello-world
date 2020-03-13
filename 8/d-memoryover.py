N=int(input())
a,b=[],[]
for i in range(1,N+1):
    if len(a) >=N : 
        print(str(a[N-1])+'/'+str(b[N-1]))
        break
    if i%2==0 :
        a+=[j for j in range(1,i+1)]
        b+=[j for j in range(i,0,-1)]
    else :
        a+=[j for j in range(i,0,-1)]
        b+=[j for j in range(1,i+1)]
