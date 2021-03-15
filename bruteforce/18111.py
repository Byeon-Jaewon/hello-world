from collections import Counter

N, M, B = map(int, input().split())

land = []
for i in range(N):
    land += (map(int, input().split()))
landsum = sum(land)
land = dict(Counter(land))
mintime = 1000000000000000000000
height = 0

for i in range(257):
    time = 0
    if (N*M*i) <= B + landsum:
        for j in land :
            if j < i :
                time += (i-j)*land[j]
            elif j > i :
                time += (j-i)*2*land[j]
        if time <= mintime:
            mintime = time
            height = i
print(mintime, height)