from collections import deque

N, K = map(int, input().split())

queue = deque()
queue.append(N)
MAX = 100001
time = [0]*MAX
while queue :
    cur = queue.popleft()
    if cur == K :
        print(time[cur])
    else :
        for i in (cur-1, cur+1, cur*2):
            if 0<= i < MAX and time[i] == 0:
                time[i] = time[cur]+1
                queue.append(i)