T=int(input())
for i in range(T) :
    a,b=[],[]
    k,n=int(input()),int(input())
    zero=[j for j in range(1,n+1)]
    for l in range(k) :
        for j in range(n-1):
            zero[j+1]+=zero[j]
    print(zero[-1])

