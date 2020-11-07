N=int(input())
aver=0; count=0 
for i in range(N) :
    x=list(map(int,input().split()))
    aver=(sum(x)-x[0])/(len(x)-1)
    for k in range(1,len(x)) :
        if x[k] > aver : count+=1
    print("%0.3f" % (float(count/x[0])*100)+"%")
    count=0
