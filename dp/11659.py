import sys

input = lambda :sys.stdin.readline().strip()
N, M = map(int, input().split())
result = []
num = list(map(int, input().split()))
dp = [0 for _ in range(N)]
for i in range(0, N):
    if i == 0:
        dp[i] = num[i]
    else :
        dp[i] = dp[i-1] + num[i]
for _ in range(M):
    a, b = map(int,input().split())
    if a == 1:
        print(dp[b-1])
    else :
        print(dp[b-1]-dp[a-2])
##for i in result :
##    print(i)