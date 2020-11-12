N, M = map(int, input().split())

check=[False]*N
lst=[]

def solve(ind):
    if ind==M:
        print(*lst)
        return
    
    for i in range(1, N+1):
           
        check[i-1]=True
        lst.append(i)
        solve(ind+1)
        lst.pop()
    
solve(0)
