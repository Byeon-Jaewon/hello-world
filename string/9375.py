from collections import Counter

T = int(input())
for j in range(T):
    n = int(input())
    closet = []
    for i in range(n):
        a, b = input().split()
        closet.append(b)
    result = 1
    C = Counter(closet)
    for i in C :
        result *= C[i] + 1
    print(result - 1)