def check(lst, n):
    if lst.count(n)==0 :
        return True
    else :
        return False
def track(lst, N, n, m):
    if n==N:
        print(lst)
    else:
        if check(lst, m)==True : 
            lst.append(m)
            track(lst, N, n+1, m)
        else :
            track(lst, N, n, m+1)

    

N,M= map(int, input().split())

lst=[]
for i in range(1, N+1):
    lst=[0]
    lst[0]=i
    track(lst, M, i+1, i)
