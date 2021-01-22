N = int(input())

lst=[]

for i in range(N) :
    lst.append(list(map(int, input().split())))

lst = sorted(lst, key = lambda x : x[1])

for i in range(N) :
    print(lst[i][0], lst[i][1])