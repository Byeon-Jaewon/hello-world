def dnc(x, y, n):
    global blue, white
    color = paper[y][x]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[j][i]:
                dnc(x, y, n//2)
                dnc(x+n//2, y, n//2)
                dnc(x, y+n//2, n//2)
                dnc(x+n//2, y+n//2, n//2)
                return
    if color==0 :
        white += 1
        return
    else :
        blue += 1
        return

N = int(input())
paper = []
white, blue = 0, 0
for _ in range(N):
    paper.append(list(map(int,input().split())))
dnc(0,0,N)
print(white)
print(blue)