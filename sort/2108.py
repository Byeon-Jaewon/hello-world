import sys
from collections import Counter

N = int(input())

tmp = []

for i in range(N) :
    tmp.append(int(sys.stdin.readline()))
tmp = sorted(tmp)
print(sum(tmp) / N)
print(tmp[N//2])
c = Counter(tmp).most_common()
if len(c) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else :
        print(c[0][0])
else :
    print(c[0][0])
print(max(tmp) - min(tmp))