a=[]
for i in range(5) :
    b=int(input())
    if b<40 : 
        a.append(40)
    else : a.append(b)
print(int(sum(a)/5))
