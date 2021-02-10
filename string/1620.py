N, M = map(int, input().split())
lst = []
ques = []
for i in range(N):
    lst.append(input())
for i in range(M):
    ques.append(input())

for i in ques:
    if i in lst:
        print(lst.index(i) + 1)
    else :
        print(lst[int(i)])