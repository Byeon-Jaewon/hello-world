N, M = map(int, input().split())
field = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cursor = [(0,0)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
for _ in range(N):
    field.append(list(map(int,input())))

while cursor :
    x,y = cursor.pop(0)

    if y == N-1 and x == M-1 :
        print(visited[y][x])
        break
    for i in range(4):
        a = x+dx[i]
        b = y+dy[i]
        if 0<=b<N and 0<=a<M :
            if visited[b][a] == 0 and field[b][a] == 1:
                visited[b][a] = visited[y][x] + 1
                cursor.append((a,b))