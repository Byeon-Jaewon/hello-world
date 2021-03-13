import sys

def push(x):
    stack.append(x)
def pop():
    if(not stack):
        return (-1)
    else :
        return stack.pop()
def size():
    return (len(stack))
def empty():
    if(not stack):
        return (1)
    else :
        return(0)
def top():
    if(not stack):
        return (-1)
    else :
         return(stack[-1])
N = int(sys.stdin.readline().rstrip())
stack = []

for i in range(N):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == "push":
        push(order[1])
    elif order[0] == "pop":
        print(pop())
    elif order[0] == "size":
        print(size())
    elif order[0] == "empty":
        print(empty())
    elif order[0] == "top":
        print(top())