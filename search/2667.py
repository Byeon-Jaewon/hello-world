def DFS(x,y):
    global cnt
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    if visited[y][x] == True :
        return 
    else :
        visited[y][x] = True
        if field[y][x] == 0 :
            return 
        if field[y][x] == 1 :
            cnt += 1
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if 0<=a<N and 0<=b<N :
                    DFS(a,b)
            return
    
        
N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int, input())))
visited = [[False]*N for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        cnt = 0
        DFS(i,j)
        if cnt != 0 :
            result.append(cnt)
result = sorted(result)
print(len(result))
for i in result :
    print(i)
