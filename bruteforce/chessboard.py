N, M = map(int,input().split())
lst=[]
minval=[]
for _ in range(N):
    lst.append(list(input()))
for i in range(0,N-7):
    for j in range(0,M-7):
            a=0
            for k in range(i,i+8):
                for l in range(j,j+8):

                    if((k-i+l-j)%2 == 0):
                        if(lst[k][l]=='B'):
                            a=a+1
                    else:
                        if(lst[k][l]=='W'):
                            a=a+1

            minval.append(int(a))


            a=0
            for k in range(i,i+8):
                for l in range(j,j+8):

                    if((k-i+l-j)%2 == 0):
                        if(lst[k][l]=='W'):
                            a=a+1
                    else:
                        if(lst[k][l]=='B'):
                            a=a+1
            minval.append(int(a))
print(min(minval))

