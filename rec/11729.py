def h_move(a,n,src,thru,dst):
    if n==1 : a.append([src, dst])
    else :
        h_move(a,n-1,src,dst,thru)
        a.append([src,dst])
        h_move(a,n-1,thru,src,dst)
n=int(input())
a=[]
h_move(a,n,1,2,3)
print(len(a))
for i in range(len(a)):
    print(a[i][0], a[i][1])
    

