N=int(input())
count=0
for i in range(N):
    a=input()
    b=[]
    result=True
    for j in range(len(a)) :
        if a[j] not in b :
            b.append(a[j])
    for k in b :
        index = a.find(k)
        print(index, a.rfind(k))
        while index != len(a)-1 and a[index]==a[index+1]:
            index+=1
        if index != a.rfind(k):
            result=False
    if result==True : count+=1

print(count)
        
        
