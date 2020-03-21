N=int(input())
a=[]
for i in range(N) :
    b=list(map(int,str(i)))
    if i+sum(b) ==N :
        a.append(i)
if a==[]:print(0)
else :
    print(min(a))
