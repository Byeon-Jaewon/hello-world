N=int(input())
count=0
for i in range(N) :
    a=list(input())
    b=[]
    for j in range(len(a)):
        if a[j] not in b :
            b.append(a[j])
    x=0
    for k in range(0,len(a)+1):
        if x>=(len(b)) : 
            count+=1
            break
        elif k>(len(a)-1) : pass
        else :
            if b[x]==a[k] : pass
            elif b[x]!=a[k] : x=x+1
print(N-count)
