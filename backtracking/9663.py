N = int(input())
a, b, c = [False]*N, [False]*(2*N-1), [False]*(2*N-1)


def solve(i):
    if i == N:
        return 1
    result = 0
    for j in range(N):
        if not (a[j] or b[i+j] or c[i-j+N-1]):
            a[j] = b[i+j]= c[i-j+N-1] = True
            result += solve(i+1)
            a[j] = b[i+j]= c[i-j+N-1] = False
    return result
print(solve(0))