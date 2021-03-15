from collections import deque
N, K = map(int, input().split())
queue = deque()
result = []
for i in range(1, N+1):
    queue.append(i)
while queue:
    for i in range(K-1):
        queue.append(queue[0])
        queue.popleft()
    result.append(queue.popleft())
print("<", end = '')
for i in range(N) :
    print(result[i], end = '')
    if i < N - 1:
        print(", ",end = '')
    else :
        print(">")