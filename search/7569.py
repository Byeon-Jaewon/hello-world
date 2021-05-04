M,N,H = map(int, input().split())
box = [[] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        box[i].append(list(map(int, input().split())))
print(box)