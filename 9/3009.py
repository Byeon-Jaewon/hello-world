a,x,y=[],[],[]
for _ in range(3):
    m,n=list(map(int,input().split()))
    a.append(m);a.append(n)
for i in range(len(a)):
    if i%2==0 : 
        if a[i] in x :
            x.remove(a[i])
        else :
            x.append(a[i])
    else : 
        if a[i] in y :
            y.remove(a[i])
        else :
            y.append(a[i])
print(x[0],y[0])
