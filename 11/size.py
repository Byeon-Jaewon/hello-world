N=int(input()) 
cm, kg=[],[]
kre=[0]*N ; cre=[0]*N
count=1
for i in range(N):
    x,y = map(int,input().split())
    kg.append(x)
    cm.append(y)
print(cm, kg)
while 0 in kre :
    kre[kg.index(max(kg))]=count
    count+=1 ; kg[kg.index(max(kg))]=0
count=1
while 0 in cre :
    cre[cm.index(max(cm))]=count
    count+=1 ; cm[cm.index(max(cm))]=0
for i in range(N) :
    if cre[i]==kre[i] : 
        print(cre[i], end=' ')
    else :
        print(2, end=' ')

