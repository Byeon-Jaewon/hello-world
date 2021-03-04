N = int(input())
count = 1
arr = []
result = []
flag = 0
for i in range(0, N):
    n = int(input())
    while (count <= n):
        arr.append(count)
        result.append('+')
        count += 1
    if (arr[-1] == n):
        arr.pop()
        result.append('-')
    else :
        flag = 1

if flag == 0 :
    for i in result:
        print(i)
else :
    print("NO")