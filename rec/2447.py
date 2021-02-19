def star(i,j) :
    while(i!=0):
        if j%3==1 and i%3==1:
            print(" ",end='')
            return None           
        i=i//3
        j=j//3
    print("*",end='')

N=int(input())
for i in range(N):
    for j in range(N):
        star(i,j)
    print("")
