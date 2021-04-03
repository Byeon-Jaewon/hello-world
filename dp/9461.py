T = int(input())

for _ in range(T):
    N = int(input())
    tri_len = [1,1,1]

    for i in range(3, N):
        tri_len.append(tri_len[i-3] + tri_len[i-2])
    print(tri_len[-1])