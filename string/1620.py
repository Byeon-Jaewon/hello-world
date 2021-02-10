import sys
N, M = map(int, sys.stdin.readline().split())
lst = []
dic = {}
ques = []
for i in range(1, N+1):
    a = sys.stdin.readline().rstrip()
    lst.append(a)
    dic[a] = i
for _ in range(M):
    ques.append(sys.stdin.readline().rstrip())
for j in ques:
    if j.isalpha():
        print(dic[j])
    elif j.isdigit() :
        print(lst[int(j)-1])