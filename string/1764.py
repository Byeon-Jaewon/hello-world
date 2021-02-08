import sys

N, M = map(int, sys.stdin.readline().split())

nh = []
ns = []
for i in range(N):
    nh.append(sys.stdin.readline())
for i in range(M):
    ns.append(sys.stdin.readline())
inter = list(set(nh) & set(ns))
inter = sorted(inter)
print(len(inter))
for i in inter:
    print(i, end='')