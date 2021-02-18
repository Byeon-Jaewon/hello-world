n=list(map(int, input().split()))
result=[]
for i in n :
    result.append(pow(i,2))
print(sum(result)%10)
