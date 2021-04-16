N = int(input())
if N == 1 or N ==2:
    print(N)
else :
    dp = [0 for _ in range(N)]
    dp[0] = 1
    dp[1] = 2
    for i in range(2, N):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[-1]%10007)