N=list(str(input()))
for i in range(len(N)) :
    N[i]=int(N[i])
N.sort(reverse=True)
for i in N :
    print(i,end='')




