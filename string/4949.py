result = []
while True:
    s = input()
    stack = []
    flag = True
    if s == '.':
        break
    for i in s:
        if i in '([':
            stack.append(i)
        elif i == ')' :
            if not stack or stack[-1]=='[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if flag == True and not stack :
        result.append('yes')
    else :
        result.append('no')
for i in result:
    print(i)