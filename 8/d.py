N=int(input())
a=[]
b=[]
if N==1 : 
    a=[1];b=[1]
elif N==2 : 
    a=[1,1];b=[1,2]
else:
    for i in range(N) :
        if len(a)==N : break
        for j in range(1,i+1):
            if len(a)==N : break
            a.append(j)
    for k in range(N) :
        if len(b)==N : break
        for l in range(k,0,-1):
            if len(b)==N : break
            b.append(l)
print(a,b)

