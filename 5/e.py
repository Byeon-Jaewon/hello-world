N=int(input())
a=list(map(int,input().split()))
m=max(a)
b=[]
for i in a :
    b.append(i/m*100)
print(sum(b)/len(b))
