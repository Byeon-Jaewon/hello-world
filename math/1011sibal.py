T=int(input())
for i in range(T) :
    x,y=map(int, input().split())
    half=(y+x)/2; j,k=1,0
    while x < y :
        x += j
        if x<=half: 
            j+=1
        else :
            if j > 1 :
                j-=1
            else : j=1
        k+=1
        print(x, j)
    print(k)
