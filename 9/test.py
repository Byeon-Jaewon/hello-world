

def sosu(N) :
    if N==1 : return False
    n=int(N**0.5)

    for i in range(2,n+1):
        if N%i==0 : return False
    return True

m,n=map(int,input().split())
for i in range(m,n+1):
    if sosu(i)==True :
        print(i)
