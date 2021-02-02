N = int(input())

tmp=[]
for i in range(N):
    tmp.append(input())
for i in range(N):
    flag=0
    for j in range(len(tmp[i])):
        if (tmp[i][j] == '('):
            flag += 1
        elif (tmp[i][j] == ')'):
            flag -= 1
        if (flag < 0):
            break
    if (flag == 0):
        print("YES")
    else :
        print("NO")