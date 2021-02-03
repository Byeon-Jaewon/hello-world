K = int(input())

tmp=[]
for i in range(K):
    a = int(input())
    if a != 0 :
        tmp.append(a)
    else :
        del tmp[-1]
print(sum(tmp))