M,N=int(input()),int(input())
count=0; a=[]
for i in range(M,N+1) :
    for j in range(1,i+1) :
        if i%j==0 : 
            count+=1
        else : pass
    if count==2 : 
        a.append(i)
    count=0
if a==[] :
    print(-1)
else : 
    print(sum(a))
    print(min(a))
