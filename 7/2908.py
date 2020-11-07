a,b = map(str,input().split())
A=list(a) ; B=list(b)
A.reverse() ; B.reverse()
aa=''.join(A) ; bb=''.join(B)
if int(aa)>int(bb) : 
    print(int(aa))
else :
    print(int(bb))

