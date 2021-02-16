def gcd(x, y):
    if y != 0:
        return gcd(y, x%y)
    else :
        return x
def lcm(x, y):
    return (x*y)//gcd(x,y)
N, M = map(int, input().split())

print(gcd(N, M))
print(lcm(N, M))