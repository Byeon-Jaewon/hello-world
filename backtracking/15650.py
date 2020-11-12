N, M = map(int, input().split())

check=[False]*N
lst=[]

def init(arr, n):
    for i in range(0, len(arr)):
        if i<n : 
            arr[i]=True
        else :
            arr[i]=False

def solve(ind):
    if ind==M:
        print(*lst)
        return
        
    for i in range(1, N+1):
        if check[i-1]==True :
            continue
        
        check[i-1]=True
        lst.append(i)
        solve(ind+1)
        lst.pop()
        init(check,i)
    

    
solve(0)
