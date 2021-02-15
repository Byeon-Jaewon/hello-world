def BinSearch(lst, val, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if lst[mid] > val :
        return BinSearch(lst, val, low, mid - 1)
    elif lst[mid] < val:
        return BinSearch(lst, val, mid + 1, high)
    else :
        return True

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))
for i in B:
    if BinSearch(A, i, 0, N-1) == True:
        print(1)
    else : 
        print(0)