# 디큐 사용
from collections import deque


def bfs(n):
    dq = deque([n])
    visited[n] = 0

    while dq:
        dx = [-1, 1]
        x = dq.popleft()
        nx = x * 2
        if nx < max_num and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            dq.appendleft(nx)
            if nx == k:
                return visited[x] + 1

        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx < max_num and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                dq.append(nx)
                if nx == k:
                    return visited[x] + 1


n, k = map(int, input().split())

max_num = 100001
visited = [-1] * max_num

bfs(n)
print(visited[k])
