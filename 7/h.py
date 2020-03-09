N=str(input())
n=list(N)
a=[]
for i in range(len(n)) :
    if (n[i]=='A')or(n[i]=='B')or(n[i]=='C')  : 
        a.append(3)
    elif (n[i]=='D')or(n[i]=='E')or(n[i]=='F') :
        a.append(4)
    elif (n[i]=='G')or(n[i]=='H')or(n[i]=='I') :
        a.append(5)
    elif (n[i]=='J')or(n[i]=='K')or(n[i]=='L') :
        a.append(6)
    elif (n[i]=='M')or(n[i]=='N')or(n[i]=="O") :
        a.append(7)
    elif (n[i]=='P')or(n[i]=='Q')or(n[i]=='R')or(n[i]=='S') :
        a.append(8)
    elif (n[i]=='T')or(n[i]=='U')or(n[i]=='V') :
        a.append(9)
    elif (n[i]=='W')or(n[i]=='X')or(n[i]=='Y')or(n[i]=='Z'):
        a.append(10)
print(sum(a))
