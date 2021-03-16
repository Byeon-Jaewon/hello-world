def solve(n) :
    if n == 0 :
        print(1, 0)
    elif n == 1 :
        print(0, 1)
    elif n == 2 :
        print(1, 1)
    else :
        tmp = 0
        zero = 0
        one = 1
        for i in range(n - 1):
            tmp = one
            one = zero + tmp
            zero = tmp
        print(zero, one)

T = int(input())

for _ in range(T):
    solve(int(input()))