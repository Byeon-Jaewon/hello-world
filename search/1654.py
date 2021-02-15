K, N = map(int, input().split())
a=[]
for _ in range(K):
    a.append(int(input()))

start = 1
end = max(a)
while (start <= end):
    mid = (start + end) // 2
    x = 0
    for i in a:
        x += i // mid
    if (x >= N):
        start = mid + 1
    elif (x < N):
        end = mid - 1
print(end)