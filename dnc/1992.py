def quadtree(x,y,n):
    cur = field[y][x]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if field[j][i] != cur :
                print('(',end='')
                quadtree(x,y,n//2)
                quadtree(x+n//2,y,n//2)
                quadtree(x,y+n//2,n//2)
                quadtree(x+n//2,y+n//2,n//2)
                print(')',end='')
                return 
    print(cur,end='')

N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int,input())))

quadtree(0,0,N)
