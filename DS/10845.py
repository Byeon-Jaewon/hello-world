import sys

def push(x) :
    queue.append(x)
def pop() :
    if not queue:
        return (-1)
    else :
        return (queue.pop(0))
def size() :
    return (len(queue))
def empty():
    if not queue:
        return (1)
    else :
        return (0)
def front() :
    if not queue :
        return (-1)
    else :
        return (queue[0])
def back() :
    if not queue :
        return (-1)
    else :
        return (queue[-1])

N = int(sys.stdin.readline().rstrip())
queue = []

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
    elif order[0] == "front":
        print(front())
    elif order[0] == "back" :
        print(back())