import sys

def push_front(x):
    deque.insert(0,x)
def push_back(x):
    deque.append(x)
def pop_front():
    if not deque:
        return (-1)
    else :
        return (deque.pop(0))
def pop_back():
    if not deque:
        return (-1)
    else :
        return (deque.pop())
def size():
    return (len(deque))
def empty():
    if not deque:
        return (1)
    else :
        return (0)
def front():
    if not deque :
        return (-1)
    else :
        return (deque[0])
def back():
    if not deque :
        return (-1)
    else :
        return (deque[-1])

N = int(sys.stdin.readline().rstrip())
deque = []

for i in range(N):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == "push_front":
        push_front(order[1])
    elif order[0] == "push_back":
        push_back(order[1])
    elif order[0] == "pop_front":
        print(pop_front())
    elif order[0] == "pop_back":
        print(pop_back())
    elif order[0] == "size":
        print(size())
    elif order[0] == "empty":
        print(empty())
    elif order[0] == "front":
        print(front())
    elif order[0] == "back" :
        print(back())