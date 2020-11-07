alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
bet=list(alphabet)
N=str(input()).upper()
a=[]
for i in range(len(bet)):
    a.append(N.count(bet[i]))
if a.count(max(a))>1 :
    print("?")
else :
    print(bet[a.index(max(a))])
