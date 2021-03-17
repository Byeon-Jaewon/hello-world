M = int(input())
S = set([])
for _ in range(M):
    order = input().rstrip().split()

    if order[0] == 'add':
        S.add(order[1])
    elif order[0] == 'remove':
        S.remove(order[1])
    elif order[0] == 'check' :
