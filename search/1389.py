from collections import deque

def BFS(num, n):
    route = [0]*n
    visited = [num]
    queue = deque()
    queue.append(num)
    while queue:
        a = queue.popleft()
        for i in relationship[a]:
            if i not in visited:
                route[i] = route[a]+1
                visited.append(i)
                queue.append(i)
    return sum(route)
        
N, M = map(int, input().split())
relationship=[[] for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    relationship[a-1].append(b-1)
    relationship[b-1].append(a-1)

result = []
for i in range(N):
    result.append(BFS(i,N))
print(result.index(min(result))+1)