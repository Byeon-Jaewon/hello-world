n = int(input())

result = 4

for i in range(int(n**0.5), int((n//4)**0.5), -1) :
    if i*i == n:
        result = 1
        break
    else :
        tmp = n - i * i
        for j in range(int(tmp**0.5), int((tmp//3)**0.5), -1):
            if i*i + j*j == n :
                result = min(result, 2)
            else :
                tmp = n - i*i - j*j
                for k in range(int(tmp**0.5), int((tmp//2)**0.5), -1):
                    if i*i + j*j + k*k == n:
                        result = min(result, 3)
print(result)