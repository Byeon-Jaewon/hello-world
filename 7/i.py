croa=["c=","c-","dz=","d-","lj","nj","s=","z="]
alpha=list("abcdefghijklmnopqrstuvwxyz=-")
count=[]
c=[]
N=str(input())
for i in range(len(alpha)) : 
    count.append(N.count(alpha[i]))
for j in range(len(croa)) :
    c.append(N.count(croa[j]))
print(sum(count)-sum(c))
