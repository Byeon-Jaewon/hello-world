while 1 != 0 :
    a=list(map(int,input().split()))
    if a[1]==0 :
        break
    m=max(a)**2
    a.remove(max(a))
    a=[i**2 for i in a]
    if sum(a)==m :
        print("right")
    else : 
        print("wrong")
    
