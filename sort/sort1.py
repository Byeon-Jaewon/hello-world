N=int(input())
a=[]
for i in range(N):
    a.append(int(input()))
a=sorted(a)
for i in range(N) :
    print(a[i])
