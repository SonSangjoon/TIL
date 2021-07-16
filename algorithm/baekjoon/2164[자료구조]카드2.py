from collections import deque

n = int(input())
dq = deque([i for i in range(1, n + 1)])

while dq:
    e = dq.popleft()

    if dq:
        e = dq.popleft()
        if dq:
            dq.append(e)
        else:
            print(e)
    else:
        print(e)