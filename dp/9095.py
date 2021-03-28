T = int(input())
nlist = []
dp = [1, 2, 4]
for _ in range(T):
    nlist.append(int(input()))
for i in range(3,max(nlist)) :
    dp.append(dp[i-1]+ dp[i-2] + dp[i-3])
for i in nlist :
    print(dp[i-1])