alpha="abcdefghijklmnopqrstuvwxyz"
bet=list(alpha)
count=[]
word=str(input())
for i in range(len(bet)) :
    re=word.find(alpha[i])
    count.append(re)

for j in range(len(count)) :
    print(count[j], end=' ')
