from collections import deque

def push(lst, x):
    lst.append(x)

def pop(lst):
    if lst:
        e = lst.popleft()
        print(e)
    else:
        print(-1)

def size(lst):
    print(len(lst))

def empty(lst):
    if lst:
        print(0)
    else:
        print(1)

def front(lst):
    if lst:
        print(lst[0])
    else:
        print(-1)

def back(lst):
    if lst:
        print(lst[-1])
    else:
        print(-1)

def solution():
    n = int(input())
    lst = deque([])
    cmd_line ={"pop": pop, 'size': size, 'empty': empty, 'front': front, 'back': back}
    cmd_set = [list(map(str, input().split())) for _ in range(n)]
    for cmd in cmd_set:
        if cmd[0] == "push":
            push(lst, cmd[1])
        else:
            cmd_line[cmd[0]](lst)
solution()