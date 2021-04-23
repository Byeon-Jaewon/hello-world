import sys
sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline()

def dfs(idx):
    visited[idx] = True
    for i in edge[idx]:
        if not visited[i]:
            dfs(i)
N, M = map(int, input().split())

edge = [[] for i in range(N)]
visited = [False] * (N)
result = 0
for _ in range(M):
    u, v = map(int,input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
for i in range(N):
    if not visited[i]:
        dfs(i)
        result += 1
print(result)