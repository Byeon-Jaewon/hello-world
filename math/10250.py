T=int(input())
for i in range(T) :
    H,W,N = map(int,input().split())
    if N%H == 0 :
        h=H
        w=N/H
    else : 
        h=N%H
        w=int(N/H+1)
    print(int(h*100 + w))

