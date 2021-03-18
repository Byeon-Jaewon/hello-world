import sys
sys.setrecursionlimit(10000)
def dfs(x, y) :
    dx = [1, -1 ,0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<= nx < N) and (0<= ny < M):
            if field[nx][ny] == True:
                field[nx][ny] = False
                dfs(nx, ny)

T = int(input())
result = []
for _ in range(T):
    M, N, K = map(int, input().split())
    count = 0
    field = [[False] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = True
    
    for i in range(N):
        for j in range(M):
            if field[i][j] == True:
                dfs(i, j)
                count += 1
    result.append(count)
for i in result:
    print(i)