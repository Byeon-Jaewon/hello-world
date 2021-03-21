def DFS(list, sp):
    if sp not in d_result :
        d_result.append(sp)
    for i in graph[sp]:
        if i not in d_result :
            d_result.append(i)
            DFS(graph[i], i)

def BFS(list, sp):
    b_result.append(sp)
    queue = [sp]
    while queue:
        cursor = queue.pop(0)
        for i in graph[cursor] :
            if i not in b_result :
                queue.append(i)
                b_result.append(i)
    


N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]
d_result = []
b_result = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

DFS(graph[V], V)
BFS(graph[V], V)
for i in d_result :
    print(i, end= ' ')
print()
for i in b_result:
    print(i, end= ' ')
