while (True):
    flag = 1
    N = input()
    if N == '0' : 
        break
    for i in range(0, int(len(N)/2)):
        if N[i] != N[-i -1]:
            flag = 0
            break
    if flag == 1 :
        print('yes')
    else :
        print('no')