N=int(input())
a=list(map(int,input().split()))
b=0
count=0
for i in range(len(a)):
    for j in range(1,int(a[i])+1):
        if (int(a[i])%j)==0 :
            count+=1
        else : pass
    if count==2 : 
        b+=1
    count=0
print(b)
