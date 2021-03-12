from sys import stdin

N = stdin.readline()
s_card = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
hm_card = list(map(int, stdin.readline().split()))

result = dict()

for i in s_card :
    try :
        result[i] += 1
    except :
        result[i] = 1
for i in hm_card :
    try :
        print(result[i], end = ' ')
    except :
        print(0, end=' ')