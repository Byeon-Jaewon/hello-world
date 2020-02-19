N = int(input())
i=0
j=0
for i in range(N) : 
    for j in range(N) : 
        if j<=i:
            print("*",end='')
    print("")
