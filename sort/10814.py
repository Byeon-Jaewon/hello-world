N = int(input())
lst= []
for i in range(N):
    [a, b] = input().split()
    lst.append([a,b])

lst= sorted(lst, key = lambda x :int(x[0]))

for i in range(N):
    print(lst[i][0], lst[i][1])