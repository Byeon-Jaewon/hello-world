N = int(input())
s_card = list(map(int, input().split()))
M = int(input())
hm_card = list(map(int, input().split()))
result = [0] * M

for i in range(M) :
    for j in s_card:
        if hm_card[i] == j :
            result[i] += 1
for i in result:
    print(i, end=' ')