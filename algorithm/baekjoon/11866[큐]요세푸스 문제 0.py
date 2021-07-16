from collections import deque

n, k = map(int, input().split())
dq = deque([str(i) for i in range(1, n + 1)])
ans = []

while dq:
    for i in range(k - 1):
        e = dq.popleft()
        dq.append(e)

    e = dq.popleft()
    ans.append(e)

print("<" + ", ".join(ans) + ">")