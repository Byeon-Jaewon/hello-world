X = int(input())
cnt = 0 
arr = [X]
def solve(a):
    list = []
    for i in a :
        list.append(i-1)
        if i % 2 == 0 :
            list.append(i//2)
        if i % 3 == 0 :
            list.append(i//3)
    return list
tmp =[]
while True:
    if X == 1 :
        break
    arr = solve(arr)
    cnt += 1
    if min(arr) == 1:
        break
print(cnt)