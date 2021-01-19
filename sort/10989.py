import sys

N = int(input())

tmp = [0] * 10001

for i in range(N) :
    num = int(sys.stdin.readline())
    tmp[num - 1] = tmp[num - 1] + 1

for i in range(10001) :
    if tmp != 0 :
        for j in range(tmp[i]) :
            print(i + 1)
