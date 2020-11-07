def selfnumber(i) : 
    one=i%10
    ten=((i-one)/10)%10
    hundred=((i-(i%100))/100)%10
    thousand=((i-(i%1000))/1000)%10
    return i+one+ten+hundred+thousand
arr=[]
for n in range(1,10001) :
    i=selfnumber(n)
    arr.append(i)

for x in range(1,10001) :
    if x in arr :
        pass
    else : print(x)
