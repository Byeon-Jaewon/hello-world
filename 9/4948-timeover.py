def fpn(n) :
    if n == 1 : return False
    for i in range(2,int(n**0.5)+1) :
        if n%i==0 : 
            return False
    return True
while 1 :
    n=int(input())
    a=[]
    if n==0 : break
    for i in range(n+1,2*n+1):
        if fpn(i)==True :
            a.append(i)
    print(len(a))

