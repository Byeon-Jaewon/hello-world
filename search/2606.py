def solve(idx):
    for i in network[idx] :
        if i not in virus :
            virus.append(i)
            solve(i)
    

C = int(input())
N = int(input())
network = [[] for i in range(C+1)]
virus = []
for _ in range(N):
    a, b = map(int,input().split())
    network[a].append(b)
    network[b].append(a)
solve(1)
print(len(virus)-1)