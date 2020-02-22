a=int(input())
b=int(input())
c=int(input())

n=a*b*c
n=str(n)
for i in range(0,10):
    print(n.count(str(i)))
