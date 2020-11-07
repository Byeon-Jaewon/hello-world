A=int(input())
B=int(input())
C=int(input())
a=A*B*C
test=list(map(int, str(a)))
count = [0,0,0,0,0,0,0,0,0,0]
for i in test :
    if i==0 :
        count[0]=count[0]+1
    elif i==1 :
        count[1]=count[1]+1
    elif i==2 : 
        count[2]=count[2]+1
    elif i==3 :
        count[3]=count[3]+1
    elif i==4 :
        count[4]=count[4]+1
    elif i==5 :
        count[5]=count[5]+1
    elif i==6 :
        count[6]=count[6]+1
    elif i==7 :
        count[7]=count[7]+1
    elif i==8 :
        count[8]=count[8]+1
    else :
        count[9]=count[9]+1
for j in count :
    print(j)
