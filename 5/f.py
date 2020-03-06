N= int(input())
count=0 ; result=0 ; RESULT=[]
for i in range(N) :
    a=list(input())
    for j in range(len(a)) :
        if a[j]=="O" :
            count+=1
            result+=count
        else :
            count=0
    RESULT.append(result)
    result=0
    count=0
for i in range(len(RESULT)) :
    print(RESULT[i])
