N, K = map(int, input().split())
coin = []
result = 0
for _ in range(N):
    coin.append(int(input()))
for i in range(N-1, -1, -1):
    if K == 0:
        break
    result += K//coin[i]
    K %= coin[i]
print(result)