N = int(input())
X = list(map(int,input().split()))
result = []
XP = sorted(list(set(X)))
dic = {XP[i] : i for i in range(len(XP))}

for i in X :
    result.append(dic[i])

for i in result :
    print(i, end = ' ')