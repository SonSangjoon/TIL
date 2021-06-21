def dfs(x, y):
    global M, N
    cnt = 0
    visited[x][y] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < M and 0 <= new_y < N:
            if visited[new_x][new_y] == 0 and default_mp[new_x][new_y] == 0:
                dfs(new_x, new_y)
                cnt += 1
                return cnt
    return cnt

M, N, n = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
default_mp = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
answer = []
cnt = 0

for r in mp:
    a, b, c, d = r[0], r[1], r[2], r[3]
    for i in range(c, d):
        for j in range(a, b):
            default_mp[i][j] = 1

for i in range(M):
    for j in range(N):
        if default_mp[i][j] == 0 and visited[i][j] == 0:
            ans = dfs(i, j)
            if ans != 0:
                answer.append(ans)

print(answer)