T = int(input())

lst=[]
for i in range(T):
    lst.append(list(map(str, input().split())))
for i in lst:
    for j in i:
        print(''.join(reversed(j)), end = ' ')
    print()