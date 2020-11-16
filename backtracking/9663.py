N = int(input())
lst=[]
MAX = N*N
count = 0
for i in range(0, MAX) :
    lst.append(False)
def init(lst):
    for i in range(MAX):
        lst[i]=False
def queen(lst, point) :
    for i in range(0, MAX):
        if(int(i/N)==(int(point/N))) :
            lst[i]=True
        if((i%N)==(point%N)):
            lst[i]=True
        if((i%N)+int(i/N)==(point%N)+int(point/N)):
            lst[i]=True
        if(int(i/N)-(i%N)==(int(point/N)-(point%N))):
            lst[i]=True
def solve(ind):
    if ind == N :
        count+=1
        return
    for i in range(MAX):
        if lst[i]==True:
            continue
        queen(lst, i)
        solve(ind+1)

solve(0)
print(count)
