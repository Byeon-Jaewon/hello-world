a=[]
for i in range(9) :
    content = int(input())
    a.append(content)
print(max(a))
print(a.index(max(a))+1)

