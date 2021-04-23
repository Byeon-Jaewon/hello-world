from collections import deque

N, K = map(int, input().split())

queue = deque()
queue.append(N)
MAX = 100001
count = 0
time = [-1]*MAX
time[N] = 0
while queue :
    cur = queue.popleft()
    if cur == K :
        count += 1
    for i in (cur-1, cur+1, cur*2):
        if 0<= i < MAX :
            if time[i] == -1 or time[i]==time[cur]+1:
                time[i] = time[cur]+1
                queue.append(i)
print(time[K])
print(count)