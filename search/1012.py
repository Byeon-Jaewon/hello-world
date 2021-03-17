T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    baechu = []
    for _ in range(K):
        baechu.append(list(map(int, input().split())))
    print(baechu)