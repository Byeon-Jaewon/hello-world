result = []
while True:
    STR = input()
    if STR == '.':
        break
    sflag = 0
    lflag = 0
    for i in STR:
        if i == '(' :
            sflag += 1
        elif i == ')' :
            sflag -= 1
        if i == '[' :
            lflag +=1 
        elif i == ']' :
            lflag -= 1
        if (sflag < 0 or lflag < 0):
            break
    if (sflag == 0 and lflag == 0):
        result.append("yes")
    else :
        result.append("no")
for i in result:
    print(i)