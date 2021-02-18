T=int(input())
for i in range(T) :
    x,y=map(int, input().split())
    j=1; k=y-x
    while True : 
        if j**2 <= k < (j+1)**2 :
            break
        j+=1
    if j**2 == k:
        print(j*2-1)
    elif j**2 < k <= j**2 + j:
        print(j*2)
    else : print(j*2+1)
