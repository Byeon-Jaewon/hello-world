a=[]
for x in range(10000) :
    if '666' in str(x) :
        a.append(x)

N=int(input())

print(a[N-1])
