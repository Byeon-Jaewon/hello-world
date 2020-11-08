a,b,c=map(int,input().split())
i,d=1,0
while d<c :
    d+=a
    if d >= c : break
    d-=b
    i+=1
print(i)
