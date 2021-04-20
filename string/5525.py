N = int(input())
M = int(input())
S = str(input())

count = 0
flag = 0
i = 0
while i < M-2 :
    if S[i]=='I' and S[i+1]=='O' and S[i+2]=='I':
        flag += 1
        if flag == N :
            count += 1
            flag -= 1
        i += 1
    else :
        flag = 0
    i+=1

print(count)