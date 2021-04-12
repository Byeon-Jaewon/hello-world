N = int(input())
P = list(map(int, input().split()))
P.sort()
result = 0
for i in range(N) :
    for j in range(i + 1) :
        result += P[j]
print(result)
