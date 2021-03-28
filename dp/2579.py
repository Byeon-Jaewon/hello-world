stair = int(input())
score_list = []
for _ in range(stair):
    score_list.append(int(input()))
for _ in range(3):
    score_list.append(0)
dp = [0, 0, 0]

dp[0] = score_list[0]
dp[1] = score_list[0]+score_list[1]
dp[2] = max(score_list[0]+score_list[2], score_list[1]+score_list[2])
if stair > 3:
    for i in range(3, stair):
        dp.append(max(score_list[i]+score_list[i-1]+dp[i-3], score_list[i]+dp[i-2]))
print(dp[stair-1])