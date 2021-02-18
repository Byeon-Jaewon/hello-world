from math import factorial

def bc(N, K) :
    if (K < 0) :
        return 0
    elif (K > N):
        return 0
    else :
        return (factorial(N) // (factorial(K)*factorial(N-K)))

N, K = map(int, input().split())

print(bc(N, K))