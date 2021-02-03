N = int(input())

tmp=[]

for i in range(N):
    a, b = map(int,input().split(','))
    tmp.append(a+b)
for i in tmp:
    print(i)