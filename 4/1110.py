a=int(input())
second = a%10
first = int((a-second)/10)
third = (first+second)%10
i=1
while 10*second+third !=a :
    first = second
    second =third
    third = (first+second)%10
    i=i+1
print(i)
