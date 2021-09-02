from sys import stdin
from collections import deque


def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    mp[x][y] = 0
    dq = deque([[x, y]])

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and mp[nx][ny]:
                mp[nx][ny] = 0
                dq.append((nx, ny))


test_case = int(input())

for test in range(test_case):
    m, n, k = map(int, stdin.readline().split())
    mp = [[0] * m for _ in range(n)]
    check = []
    ans = 0

    for _ in range(k):
        y, x = map(int, stdin.readline().split())
        mp[x][y] = 1
        check.append((x, y))

    for x, y in check:

        if mp[x][y]:
            bfs(x, y)
            ans += 1

    print(ans)
