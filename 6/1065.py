def han(x) :
    ar=[]
    if x<100 :
        return x
    else :
        count = 99
        for i in range(100,x+1) :
            ar=str(i)
            if (int(ar[2])-int(ar[1])) == (int(ar[1])-int(ar[0])) :
                count=count+1
        return count

N=int(input())
print(han(N))

