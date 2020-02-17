import sys


x=int(input())
result=[]
i=0
for i in range(0,x) :
    a,b = map(int, sys.stdin.readline().split())
    result.append(a+b)
    i=i+1
j=0
for j in result : 
    print(j)
    j=j+1

