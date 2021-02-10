lst = []
for i in range(5):
    lst.append(input())
for i in range(0,15):
    for j in range(0, 5):
        if i >= len(lst[j]) :
            continue
        print(lst[j][i], end='')