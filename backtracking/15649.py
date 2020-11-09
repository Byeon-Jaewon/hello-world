N, M= map(int, input().split())

check=[False]*N
lst=[]

def solve(ind):
    if ind==M :
        print(*lst)
        return
    for i in range(1, N+1):
        if check[i-1] == True :
            continue
        check[i-1]=True
        lst.append(i)
        solve(ind+1)
        lst.pop()
        check[i-1]=False
solve(0)
