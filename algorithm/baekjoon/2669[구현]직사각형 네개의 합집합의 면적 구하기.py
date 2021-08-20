visited = [[0] * 100 for _ in range(100)]
ans = 0

for _ in range(4):
    x, y, X, Y = map(int, input().split())
    for i in range(X - x):
        for j in range(Y - y):
            if not visited[x + i][y + j]:
                visited[x + i][y + j] += 1
                ans += 1
print(ans)