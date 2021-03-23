N, M = map(int, input().split())

password = {}
result = []
for _ in range(N):
    site, pw = map(str, input().split())
    password[site] = pw
for _ in range(M):
    result.append(password[input()])
for i in result:
    print(i)