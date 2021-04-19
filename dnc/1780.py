def check(x,y,n,cur):
    if n == 1:
        return True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if field[j][i] != cur:
                return False
    return True
def dnc(x,y,n):
    cur = field[y][x]
    if check(x,y,n,cur):
        result[cur] += 1
    else :
        k = n//3
        dnc(x,y,k)
        dnc(x+k,y,k)
        dnc(x+2*k,y,k)
        dnc(x,y+k,k)
        dnc(x+k,y+k,k)
        dnc(x+2*k,y+k,k)
        dnc(x,y+2*k,k)
        dnc(x+k,y+2*k,k)
        dnc(x+2*k,y+2*k,k)
        return

N = int(input())
field = []
for _ in range(N) :
    field.append(list(map(int, input().split())))
result = {-1 : 0, 0 : 0, 1 : 0}
dnc(0,0,N)

print(result[-1])
print(result[0])
print(result[1])