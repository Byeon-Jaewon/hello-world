A="***"
B="* *"
C="   "
def star(i,j) :
    if j%3==1 and i//3%3==1:
        print(C,end='')
    elif i%3==1:
        print(B,end='')
    else :
        print(A,end='')
N=int(input())
for i in range(N):
    for j in range(N//3):
        star(i,j)
    print("")
