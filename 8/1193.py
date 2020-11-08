N=int(input())
i=1
while N>i :
    N -= i
    i += 1
if i%2==1 :
    a=i-N+1
    b=N
else :
    a=N
    b=i-N+1
print(a,'/',b,sep='')
