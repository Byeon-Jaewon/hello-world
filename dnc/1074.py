N, r, c = map(int, input().split())
point = 0
while N > 0 :
    border = 2**N//2
    if N > 1:
        if r < border and c >= border:
            point += border**2
            c -= border
        elif r >= border and c < border:
            point += (border**2) * 2
            r -= border
        elif r >= border and c >= border :
            point += (border**2) * 3
            r -= border
            c -= border


    if N == 1:
        if r == 0 and c == 1:
            point += 1
        elif r == 1 and c == 0:
            point += 2
        elif r == 1 and c == 1:
            point += 3
    N -= 1
print(point)