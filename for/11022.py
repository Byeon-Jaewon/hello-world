T = int(input())
num = 1
for _ in range(T) :
    a,b = map(int, input().split())
    print("Case #%s: %s + %s = %s" %(num,a,b, a+b))
    num=num+1
