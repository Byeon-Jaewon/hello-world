N=int(input())
for i in range(N) :
    a,b = input().split()
    A=int(a); B=list(b)
    for j in range(len(B)) :
        print(B[j]*A, end='')
    print()
    
