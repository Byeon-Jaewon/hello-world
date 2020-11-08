N=int(input())
a=[]
for i in range(0,int(N/3)+1) :
    for j in range(0,int(N/5)+1) :
        if (3*i+5*j)==N : 
            a.append(i+j)
        else : pass
if a==[] : 
    print(-1)
else :
    print(min(a))
