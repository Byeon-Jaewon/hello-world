N=int(input())
if N==1 : print(1)
else:
    a=[]
    re=1
    for i in range(N) :
        if re>=N : break
        re=re+6*i
        a.append(re)
    print(len(a))
