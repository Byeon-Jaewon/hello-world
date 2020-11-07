a=[]
for _ in range(10) :
    content=int(input())
    a.append(content)
mod=[]
for i in a :
    mod.append(i%42)
mod=list(set(mod))
print(len(mod))
