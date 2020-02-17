n= input()
n= int(n)
result = []
i=0
for i in range(0, n) : 
    a, b = map(int, input().split())
    result.append(a+b)
    i=i+1
j=0
for j in result : 
    print(j)
    j+1
