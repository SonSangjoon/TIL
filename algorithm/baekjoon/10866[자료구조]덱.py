from collections import deque


def push_front(lst, x):
    lst.appendleft(x)


def push_back(lst, x):
    lst.append(x)


def pop_front(lst):
    if lst:
        e = lst.popleft()
        print(e)
    else:
        print(-1)


def pop_back(lst):
    if lst:
        e = lst.pop()
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
    cmd_line = {
        "pop_front": pop_front,
        "pop_back": pop_back,
        "size": size,
        "empty": empty,
        "front": front,
        "back": back,
    }
    cmd_set = [list(map(str, input().split())) for _ in range(n)]
    for cmd in cmd_set:
        if cmd[0] == "push_front":
            push_front(lst, cmd[1])
        elif cmd[0] == "push_back":
            push_back(lst, cmd[1])
        else:
            cmd_line[cmd[0]](lst)

solution()